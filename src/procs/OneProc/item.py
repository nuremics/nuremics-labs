import os
import attrs
import pandas as pd
from pathlib import Path

from nuremics import Process
from procs.OneProc import utils


@attrs.define
class OneProc(Process):
    """
    Generate and plot a regular polygon shape.

    Pipeline
    --------
        1. operation1
            Generate the 2D coordinates of a regular polygon (given radius and number of sides).
        2. operation2
            Plot the shape with a title read from an external file.

    Input parameters
    ----------------
        param1 : float
            Radius of the polygon.
        param2 : int
            Number of sides of the polygon.

    Input paths
    -----------
        path1 : txt
            Path to a text file containing the plot title.

    Internal variables
    ------------------
        variable : pd.DataFrame
            Stores the generated polygon coordinates with columns ['X', 'Y'].

    Outputs (stored in self.output_paths)
    -------
        out1 : csv
            File containing the X/Y coordinates of the polygon vertices.
        out2 : png
            Image of the plotted polygon figure.
    """

    # Parameters
    param1: float = attrs.field(init=False, metadata={"input": True})
    param2: int = attrs.field(init=False, metadata={"input": True})
  
    # Paths
    path1: Path = attrs.field(init=False, metadata={"input": True}, converter=Path)

    # Internal
    variable: pd.DataFrame = attrs.field(init=False)

    def __call__(self):
        super().__call__()

        self.operation1()
        self.operation2()

    def operation1(self):
        """
        Generate the 2D coordinates of a regular polygon (given radius and number of sides).

        Uses
        ----
            param1
            param2
        
        Modifies
        --------
            variable
        
        Generates
        ---------
            out1
        """

        # Create shape points
        df_points = utils.create_shape(
            radius=self.param1,
            n_sides=self.param2,
        )
        self.variable = df_points

        # Save coordinates to CSV file
        df_points.to_csv(self.output_paths["out1"])

    def operation2(self):
        """
        Plot the shape with a title read from an external file.

        Uses
        ----
            path1
            variable

        Generates
        ---------
            out2
        """

        # Read plot title from file
        with open(self.path1, "r", encoding="utf-8") as f:
            text = f.read()

        # Plot and save figure
        utils.plot_shape(
            df_points=self.variable,
            title=text,
            filename=self.output_paths["out2"],
            verbose=self.verbose,
        )


if __name__ == "__main__":
    
    # Define working directory
    working_dir = Path(os.environ["WORKING_DIR"]) / "ONE_APP/Study1/1_OneProc/Test1"

    # Go to working directory
    os.chdir(working_dir)

    # Create dictionary containing input data
    dict_inputs = {
        "param1": 0.5,
        "param2": 3,
        "path1": Path(os.environ["WORKING_DIR"])/"ONE_APP/study1/0_inputs/input1.txt",
    }
    
    # Create process
    process = OneProc(
        dict_inputs=dict_inputs,
        set_inputs=True,
    )
    process.output_paths["out1"] = "output1.csv"
    process.output_paths["out2"] = "output2.png"

    # Run process
    process()
    process.finalize()