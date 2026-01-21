import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from typing import Optional

from importlib.resources import files
from nuremics_labs.ops.general.plotting import (
    insert_image_into_plot,
)


def generate_polygon_shape(
    radius: float,
    n_sides: int,
    filename: Optional[str] = None,
) -> pd.DataFrame:
    """
    Generate the 2D coordinates of a regular polygon.

    Parameters
    ----------
    radius : float
        Radius (m) of the circumscribed circle of the polygon.
    n_sides : int
        Number of sides of the polygon.
    filename : str, optional
        If defined, coordinates are saved to a CSV file with the provided filename.

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

    # Save coordinates to CSV file
    if filename is not None:
        df_points.to_csv(filename)
    
    return df_points


def plot_polygon_shape(
    df_points: pd.DataFrame,
    title: str,
    filename: str,
    silent: bool = False,
) -> None:
    """
    Plot a closed 2D polygon from a set of points.

    Parameters
    ----------
    df_points : pd.DataFrame
        DataFrame with columns '['X', 'Y'] representing the polygon vertices.
    title : str
        Title of the plot.
    silent : bool (default is False)
        If False, the plot is displayed on screen.
    filename : str
        Path to save the plot image (e.g., "shape.png").
    """
    
    # Append the first point to the end to close the polygon
    df_points = pd.concat(
        objs=[df_points, df_points.iloc[[0]]],
        ignore_index=True,
    )

    # Create figure and axis
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
    ax.set_aspect("equal")
    ax.grid(True)

    # Insert NUREMICS logo in plot background
    insert_image_into_plot(
        img_path=files("nuremics.resources").joinpath("logo.png"),
        fig=fig,
        ax=ax,
        alpha=0.3,
        scale=0.8,
    )

    # Save the figure to the specified filename
    fig.savefig(filename, dpi=300)

    # Display the plot in a window if silent mode is disabled
    if not silent:
        plt.show()
    
    # Close the figure to release memory
    plt.close(fig)