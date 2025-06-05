import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def create_shape(
    radius: float,
    n_sides: int,
) -> pd.DataFrame:
    """
    Generates the coordinates of a regular polygon.

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


def plot_shape(
    df_points: pd.DataFrame,
    title: str,
    filename: str,
    verbose: bool = True,
) -> None:
    """
    Plots a closed 2D polygon from a set of points and saves the figure as a PNG file.

    Parameters
    ----------
    df_points : pd.DataFrame
        DataFrame with columns 'X' and 'Y' representing the polygon vertices.
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

    # Plot the polygon with red lines and circular markers
    plt.plot(df_points["X"], df_points["Y"], "r-o")

    # Set equal aspect ratio and axis labels
    plt.gca().set_aspect("equal")
    plt.title(title)
    plt.xlabel("x")
    plt.ylabel("y")

    # Save the figure to the specified filename
    plt.savefig(filename, dpi=300)

    # Show the plot if requested
    if verbose:
        plt.show()
    
    # Close the figure to release memory
    plt.close()