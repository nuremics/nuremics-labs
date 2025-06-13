import sys
import io

stdout_orig = sys.stdout
sys.stdout = io.StringIO()
import pygame
sys.stdout = stdout_orig

import pymunk
import pymunk.pygame_util
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def run_model(
    df_points: pd.DataFrame,
    mass: float,
    gravity: float,
    h0: float,
    v0: float,
    angle: float,
    timestep: float,
    fps: int = 60,
    window_size: int = 600,
    verbose: bool = True,
) -> pd.DataFrame:
    """
    Simulates the motion of a 2D rigid body under gravity using pymunk and pygame.

    A polygonal rigid body is launched with a given initial speed and angle from an initial height.
    The simulation is run using the pymunk physics engine, and displayed using pygame. The environment
    includes a static horizontal plane and a vertical wall forming a corner.

    The simulation runs until a predefined final time or until the user closes the window.

    During the simulation, the body's position is recorded at each time step into a DataFrame,
    but only until the first contact with the horizontal ground occurs.

    Parameters
    ----------
    df_points : pd.DataFrame
        2D coordinates of the polygon defining the shape of the body (in its local frame).
    mass : float
        Mass of the body.
    gravity : float
        Gravitational acceleration.
    h0 : float
        Initial vertical position of the body's center.
    v0 : float
        Initial velocity magnitude.
    angle : float
        Launch angle in degrees (from horizontal).
    timestep : float
        Time increment for physics simulation steps (in seconds).
    fps : int, optional (default is 60)
        Frame rate for the visual simulation when verbose is True (in frames per second).
    window_size : int, optional (default is 600)
        Size in pixels of the square pygame window for visual simulation.
    verbose : bool, optional (default is True)
        If True, displays the simulation using pygame.
        If False, runs silently.

    Returns
    -------
    pd.DataFrame
        A DataFrame with columns ['t', 'x_model', 'y_model'], containing the trajectory of the body
        from t=0 until the first contact with the ground.
    """

    # Prepare an empty DataFrame to store trajectory points
    trajectory = pd.DataFrame(columns=["t", "x_model", "y_model"])

    # Compute initial velocity components
    vx = v0*np.cos(np.radians(angle))
    vy = v0*np.sin(np.radians(angle))

    # Reset frame rate depending on timestep setting
    fps = min(fps, int(1/timestep))
    
    # Compute theoretical flight characteristics (time, distance, height)
    t_flight, d_flight, h_max = compute_analytical_characteristics(
        v0=v0,
        h0=h0,
        angle=angle,
        gravity=gravity,
    )

    # Initialize simulation state
    contact = False
    running = True
    current_time = 0.0
    dt = timestep           # Time step (s)
    t_final = t_flight+2.0  # Final simulation time

    # Define visualization scale and window size
    metric = window_size/max((d_flight+4.0), (h_max+3.0))
    window_height = window_size
    window_width = window_size

    # Initialize pygame and pymunk rendering
    if verbose:
        pygame.init()
        screen = pygame.display.set_mode((window_height, window_width))
        clock = pygame.time.Clock()
        draw_options = pymunk.pygame_util.DrawOptions(screen)
        draw_options.transform = pymunk.Transform(
            a=metric,
            b=0,
            c=0,
            d=-metric,
            tx=1.5*metric,
            ty=window_height-2.0*metric,
        )

    # Create pymunk simulation space with gravity
    space = pymunk.Space()
    space.gravity = (0, gravity)

    # Create static ground segment
    segment_ground = pymunk.Segment(
        body=space.static_body,
        a=(d_flight-1.0, -0.5),
        b=(d_flight+1.0, -0.5),
        radius=0.5
    )
    segment_ground.friction = 1.0
    space.add(segment_ground)

    # Create static vertical wall forming a corner
    segment_wall = pymunk.Segment(
        body=space.static_body,
        a=(d_flight+1.0, -0.5),
        b=(d_flight+1.0, 1.5),
        radius=0.5
    )
    segment_wall.friction = 1.0
    space.add(segment_wall)

    # Create the dynamic body from shape and add it to the space
    shape:pymunk.Poly = create_body(
        space=space,
        points=df_points,
        position=(0.0, h0),
        mass=mass,
        friction=1.0,
        velocity=(vx, vy),
    )

    # Main simulation loop
    while running:
        
        # Handle user window events (e.g., quit)
        if verbose:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Clear the screen and draw the current state
            screen.fill((240, 240, 240))
            space.debug_draw(draw_options)

            # Update the display and timing
            pygame.display.flip()
            clock.tick(fps)

        # Advance physics simulation by one step
        space.step(dt)
        current_time += dt

        # Record trajectory before contact
        try:
            shape.shapes_collide(segment_ground)
            contact = True
        except:
            if not contact:
                pos = shape.body.position
                new_row = {"t": current_time, "x_model": pos.x, "y_model": pos.y}
                trajectory.loc[len(trajectory)] = new_row

        # Stop simulation after final time
        if current_time > t_final:
            running = False

    # Clean up the pygame window
    if verbose:
        pygame.quit()

    return trajectory


def create_body(
    space: pymunk.Space,
    points: pd.DataFrame,
    position: tuple[float, float],
    mass: float,
    friction: float,
    velocity: tuple[float, float],
) -> pymunk.Poly:
    """
    Creates and adds a polygonal rigid body to a Pymunk space.

    The shape of the body is defined by a set of 2D points provided in a DataFrame.
    The shape is automatically centered on its centroid. The resulting body is assigned
    a given mass, friction coefficient, initial position, and velocity.

    Parameters
    ----------
    space : pymunk.Space
        The Pymunk physics simulation space to which the body will be added.
    points : pd.DataFrame
        A DataFrame containing the 2D coordinates of the polygon vertices.
        It must include columns "X" and "Y" representing the local coordinates of the shape.
    position : tuple[float, float]
        The initial (x, y) position of the center of mass of the body in world coordinates.
    mass : float
        Mass of the rigid body.
    friction : float
        Friction coefficient applied to the polygon shape.
    velocity : tuple[float, float]
        Initial velocity of the body as (vx, vy).

    Returns
    -------
    pymunk.Poly
        The Pymunk polygon shape object that was created and added to the space.
    """
    
    # Extract point coordinates from DataFrame
    x_coords = points["X"].tolist()
    y_coords = points["Y"].tolist()
    point_list = list(zip(x_coords, y_coords))

    # Compute the centroid to center the shape
    cx = sum(x_coords) / len(x_coords)
    cy = sum(y_coords) / len(y_coords)

    # Center the coordinates around the centroid (local reference frame)
    centered_points = [(x - cx, y - cy) for x, y in point_list]
    
    # Create the body with specified mass and moment of inertia
    body = pymunk.Body(1, pymunk.moment_for_poly(mass, centered_points))
    body.position = position   # Set initial position
    body.velocity = velocity   # Set initial velocity

    # Create the polygon shape and set its friction
    shape = pymunk.Poly(body, centered_points)
    shape.friction = friction

    # Add the body and its shape to the simulation space
    space.add(body, shape)

    return shape


def compute_analytical_characteristics(
    v0: float,
    h0: float,
    angle: float,
    gravity: float,
) -> tuple[float, float, float]:
    """
    Computes the analytical flight characteristics of a projectile launched from a given height.

    This function calculates the total flight time, horizontal distance (range), and maximum height
    reached by a projectile launched with an initial speed and angle from a specified vertical height.

    Parameters
    ----------
    v0 : float
        Initial velocity magnitude (m/s).
    h0 : float
        Initial vertical position of the projectile (m).
    angle : float
        Launch angle in degrees (0° is horizontal).
    gravity : float
        Gravitational acceleration (m/s²). Can be positive (upward) or negative (downward).

    Returns
    -------
    tuple[float, float, float]
        A tuple containing:
        - t_flight : float, total time of flight until hitting the ground (s)
        - d_flight : float, horizontal distance travelled (m)
        - h_max : float, maximum vertical position reached (m)
    """
    
    # Use absolute value to ensure positive gravity for calculation
    g = np.abs(gravity)

    # Compute velocity components
    vsin = v0*np.sin(np.radians(angle))  # Vertical component
    vcos = v0*np.cos(np.radians(angle))  # Horizontal component
    
    # Total flight time until the projectile reaches the ground
    t_flight = (vsin+np.sqrt(vsin**2+2*g*h0))/g

    # Horizontal distance travelled during flight
    d_flight = vcos*t_flight

    # Maximum height reached during the trajectory
    h_max = h0+vsin**2/(2*g)

    return t_flight, d_flight, h_max


def compute_analytical_trajectory(
    df: pd.DataFrame,
    v0: float,
    h0: float,
    angle: float,
    gravity: float,
) -> pd.DataFrame:
    """
    Computes the analytical trajectory of a projectile and appends the results to a DataFrame.

    For each time 't' in the input DataFrame, this function calculates the theoretical
    x and y positions of a projectile launched from an initial height 'h0' with velocity 'v0'
    at an angle 'angle', under a constant gravitational acceleration.

    The analytical expressions used are:
        x(t) = v0 * cos(angle) * t
        y(t) = h0 + v0 * sin(angle) * t + 0.5 * gravity * t²

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing a time column 't' (in seconds).
    v0 : float
        Initial velocity magnitude (m/s).
    h0 : float
        Initial vertical position (m).
    angle : float
        Launch angle in degrees (0° is horizontal).
    gravity : float
        Gravitational acceleration (m/s²). Can be positive (upward) or negative (downward).

    Returns
    -------
    pd.DataFrame
        A copy of the input DataFrame with two new columns:
        - 'x_theory': Theoretical x position at each time step.
        - 'y_theory': Theoretical y position at each time step.
        The index of the DataFrame is set to 't'.
    """

    # Initialize new columns for analytical (theoretical) trajectory
    df["x_theory"] = np.nan
    df["y_theory"] = np.nan

    # Loop through each time point and compute the x and y positions
    for idx, t in enumerate(df["t"]):

        # Compute horizontal position using uniform linear motion
        x = v0*np.cos(np.radians(angle))*t
        # Compute vertical position using uniformly accelerated motion
        y = h0+v0*np.sin(np.radians(angle))*t+0.5*gravity*t**2
        
        # Store computed values in the DataFrame
        df.loc[idx, "x_theory"] = x
        df.loc[idx, "y_theory"] = y
    
    # Set the time column as index for convenience in plotting or analysis
    df.set_index(
        keys="t",
        inplace=True,
    )
    
    return df


def plot_comparison(
    df: pd.DataFrame,
    filename: str,
    verbose: bool = True,
) -> None:
    """
    Plots and saves a comparison between the theoretical and simulated projectile trajectories.

    This function takes a DataFrame containing theoretical and model-based (x, y) trajectories,
    generates a 2D plot comparing them, and saves the figure to the specified file.
    The plot can optionally be displayed interactively.

    Parameters
    ----------
    df : pd.DataFrame
        DataFrame containing the columns:
        - 'x_theory', 'y_theory': Theoretical trajectory coordinates.
        - 'x_model', 'y_model': Model/simulated trajectory coordinates.
    filename : str
        Path where the output plot image will be saved.
    verbose : bool, optional (default is True)
        If True, the plot will be displayed interactively.
    """

    # Plot theoretical trajectory (solid red line)
    plt.plot(df["x_theory"], df["y_theory"], "k", label="Theory")

    # Plot model/simulated trajectory (dashed blue line)
    plt.plot(df["x_model"], df["y_model"], "--r", label="Model")
    
    # Set title and axis labels
    plt.title("(x, y) trajectory: model vs. theory")
    plt.xlabel("x")
    plt.ylabel("y")
    
    # Add legend and grid
    plt.legend()
    plt.grid(True)

    # Keep aspect ratio equal for visual accuracy
    plt.axis("equal") 

    # Save the plot to the specified file (with high resolution)
    plt.savefig(filename, dpi=300)

    # Display the plot in a window if verbose mode is enabled
    if verbose:
        plt.show()

    # Close the figure to release memory
    plt.close()