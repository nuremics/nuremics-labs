import os
import attrs
import pandas as pd
from pathlib import Path

from nuremics import Process
from nuremics_labs.ops.general import polygon_geometry


@attrs.define
class PolygonGeometryProc(Process):
    """
    Generate and plot a regular 2D polygon shape.

    Process
    -------
        A/ generate_polygon_shape
            Generate the 2D coordinates of a regular polygon.
        B/ plot_polygon_shape
            Plot a closed 2D polygon from a set of points.

    Input parameters
    ----------------
        radius : float
            Radius (m) of the circumscribed circle of the polygon.
        n_sides : int
            Number of sides of the polygon.

    Input paths
    -----------
        title_file : txt
            File containing the plot title of the 2D polygon shape.

    Outputs
    -------
        coords_file : csv
            File containing the X/Y coordinates of the polygon vertices.
        fig_file : png
            Image of the plotted polygon figure.

    Internal variables
    ------------------
        df_points : pd.DataFrame
            Stores the generated polygon coordinates with columns ['X', 'Y'].
    """

    # Parameters
    radius: float = attrs.field(init=False, metadata={"input": True})
    n_sides: int = attrs.field(init=False, metadata={"input": True})
  
    # Paths
    title_file: Path = attrs.field(init=False, metadata={"input": True}, converter=Path)

    # Outputs
    coords_file: Path = attrs.field(init=False, metadata={"output": True}, converter=Path)
    fig_file: Path = attrs.field(init=False, metadata={"output": True}, converter=Path)

    # Internal
    df_points: pd.DataFrame = attrs.field(init=False)

    def __call__(self):
        super().__call__()

        self.generate_polygon_shape()
        self.plot_polygon_shape()

    def generate_polygon_shape(self):
        """
        Generate the 2D coordinates of a regular polygon.

        Uses
        ----
            radius
            n_sides
        
        Modifies
        --------
           df_points
        
        Generates
        ---------
            coords_file
        """

        # Create shape points and save coordinates to CSV file
        self.df_points = polygon_geometry.generate_polygon_shape(
            radius=self.radius,
            n_sides=self.n_sides,
            filename=self.coords_file,
        )

    def plot_polygon_shape(self):
        """
        Plot a closed 2D polygon from a set of points.

        Uses
        ----
            title_file
            df_points

        Generates
        ---------
            fig_file
        """

        # Read plot title from file
        with open(self.title_file, "r", encoding="utf-8") as f:
            text = f.read()

        # Plot and save figure
        polygon_geometry.plot_polygon_shape(
            df_points=self.df_points,
            title=text,
            filename=self.fig_file,
            silent=self.silent,
        )


if __name__ == "__main__":
    
    # ================================================================== #
    #                      USER-DEFINED PARAMETERS                       #
    #              >>>>> TO BE EDITED BY THE OPERATOR <<<<<              #
    # ================================================================== #

    # Working directory
    working_dir = Path(r"...")
    
    # Input parameters
    radius = 0.5
    n_sides = 3
    
    # Input paths
    title_file = Path(r"...") / "plot_title.txt"

    # Output paths
    coords_file = "points_coordinates.csv"
    fig_file = "polygon_shape.png"

    # ================================================================== #

    # Go to working directory
    os.chdir(working_dir)

    # Create dictionary containing input data
    dict_inputs = {
        "radius": radius,
        "n_sides": n_sides,
        "title_file": title_file,
        "coords_file": coords_file,
        "fig_file": fig_file,
    }
    
    # Create process
    process = PolygonGeometryProc(
        dict_inputs=dict_inputs,
        set_inputs=True,
    )

    # Run process
    process()
    process.finalize()