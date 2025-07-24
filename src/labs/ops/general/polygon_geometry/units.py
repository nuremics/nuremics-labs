import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def generate_polygon_shape(
    radius: float,
    n_sides: int,
) -> pd.DataFrame:
    """
    Generate the 2D coordinates of a regular polygon.

    Parameters
    ----------
    radius : float
        The radius of the circumscribed circle of the polygon.
    n_sides : int
        The number of sides (vertices) of the polygon.

    Returns
    -------
    pd.DataFrame
        A DataFrame with columns 'X' and 'Y' representing
        the 2D coordinates of the polygon vertices in counter-clockwise order.
        The polygon is centered at the origin (0, 0).
    """
    
    # Compute the coordinates of each vertex
    points = [
        (radius * np.cos(2*np.pi*i/n_sides),
         radius * np.sin(2*np.pi*i/n_sides))
        for i in range(n_sides)
    ]

    # Create a DataFrame from the list of points
    df_points = pd.DataFrame(
        data=np.array(points),
        columns=["X", "Y"],
    )
    
    return df_points


def plot_polygon_shape(
    df_points: pd.DataFrame,
    title: str,
    filename: str,
    verbose: bool = True,
) -> None:
    """
    Plot a closed 2D polygon from a set of points.

    Parameters
    ----------
    df_points : pd.DataFrame
        DataFrame with columns '['X', 'Y'] representing the polygon vertices.
    title : str
        Title of the plot.
    verbose : bool
        If True, the plot is displayed on screen.
    filename : str
        Path to save the plot image (e.g., "shape.png").
    """
    
    # Append the first point to the end to close the polygon
    df_points = pd.concat(
        objs=[df_points, df_points.iloc[[0]]],
        ignore_index=True,
    )

    # Define plot
    fig, ax = plt.subplots()

    # Plot the polygon shape
    line, = ax.plot(df_points["X"], df_points["Y"],
        linewidth=2.0,
        color="#3398db",
        marker="o",
        markersize=10,
        zorder=3,
    )
    line.set_visible(True)

    # Set title and axis labels
    ax.set_title(title, fontsize=14)
    ax.set_xlabel("x (m)", fontsize=14)
    ax.set_ylabel("y (m)", fontsize=14)
    
    # Set equal aspect ratio and grid
    ax.set_aspect("equal", adjustable="datalim")
    ax.autoscale_view()
    ax.grid(True)

    # Save the figure to the specified filename
    fig.savefig(filename, dpi=300)

    # Show the plot if requested
    if verbose:
        plt.show()
    
    # Close the figure to release memory
    plt.close(fig)