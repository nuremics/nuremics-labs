import os
import attrs
import pandas as pd
from pathlib import Path

from nuremics import Process
from labs.ops.general.polygon_geometry import units


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
            The radius of the circumscribed circle of the polygon.
        n_sides : int
            The number of sides (vertices) of the polygon.

    Input paths
    -----------
        title_file : txt
            File containing the plot title of the 2D polygon shape.

    Internal variables
    ------------------
        df_points : pd.DataFrame
            Stores the generated polygon coordinates with columns ['X', 'Y'].

    Outputs (stored in self.output_paths)
    -------
        coords_file : csv
            File containing the X/Y coordinates of the polygon vertices.
        fig_file : png
            Image of the plotted polygon figure.
    """

    # Parameters
    radius: float = attrs.field(init=False, metadata={"input": True})
    n_sides: int = attrs.field(init=False, metadata={"input": True})
  
    # Paths
    title_file: Path = attrs.field(init=False, metadata={"input": True}, converter=Path)

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

        # Create shape points
        self.df_points = units.generate_polygon_shape(
            radius=self.radius,
            n_sides=self.n_sides,
        )

        # Save coordinates to CSV file
        self.df_points.to_csv(self.output_paths["coords_file"])

    def plot_polygon_shape(self):
        """
        Plots a closed 2D polygon from a set of points.

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
        units.plot_polygon_shape(
            df_points=self.df_points,
            title=text,
            filename=self.output_paths["fig_file"],
            verbose=self.verbose,
        )


if __name__ == "__main__":
    
    # Define working directory
    working_dir = Path("...")   # to be edited

    # Go to working directory
    os.chdir(working_dir)

    # Create dictionary containing input data
    dict_inputs = {
        "radius": 0.5,
        "n_sides": 3,
        "title_file": Path(".../plot_title.txt"),   # to be edited
    }
    
    # Create process
    process = PolygonGeometryProc(
        dict_inputs=dict_inputs,
        set_inputs=True,
    )

    # Define output paths
    process.output_paths["coords_file"] = "points_coordinates.csv"
    process.output_paths["fig_file"] = "polygon_shape.png"

    # Run process
    process()
    process.finalize()