import os
import attrs
from pathlib import Path

from nuremics import Process
from labs.apps.general.BASE_APP.procs.SecondProc.ops import (
    operation,
)


@attrs.define
class SecondProc(Process):
    """
    Description of the Proc.

    Process
    -------
        A/ operation
            Description of the operation.
        B/ ...
            ...

    Input parameters
    ----------------
        param : int
            Description of the parameter.

    Input paths
    -----------
        infile : txt
            Description of the file.

    Internal variables
    ------------------
        variable : bool
            Description of the variable.

    Outputs (stored in self.output_paths)
    -------
        outfolder : folder
            'output1.txt' : Description of the file.
            'output2.txt' : Description of the file.
    """

    # Parameters
    # param: int = attrs.field(init=False, metadata={"input": True})

    # Paths
    infile: Path = attrs.field(init=False, metadata={"input": True}, converter=Path)

    # Internal
    variable: bool = attrs.field(init=False)

    def __call__(self):
        super().__call__()

        self.operation()

    def operation(self):
        """
        Description of the operation.

        Uses
        ----
            param
            infile
        
        Modifies
        --------
           variable
        
        Generates
        ---------
            outfolder/output1.txt
            outfolder/output2.txt
        """

        with open(self.infile) as file:
            content = file.read()

        Path(self.output_paths["outfolder"]).mkdir(
            exist_ok=True,
            parents=True,
        )

        self.variable = operation(
            content=content,
            outfile1=os.path.join(self.output_paths["outfolder"], "output1.txt"),
            outfile2=os.path.join(self.output_paths["outfolder"], "output2.txt"),
            # param=self.param,
        )

        print(f"Internal Variable: {self.variable}")


if __name__ == "__main__":

    # ================================================================== #
    #                      USER-DEFINED PARAMETERS                       #
    #              >>>>> TO BE EDITED BY THE OPERATOR <<<<<              #
    # ================================================================== #

    # Working directory
    working_dir = Path(r"...")

    # Input parameters
    param = 14

    # Input paths
    infile = Path(r"...") / "output.txt"

    # Output paths
    outfolder = "output"

    # ================================================================== #

    # Go to working directory
    os.chdir(working_dir)

    # Create dictionary containing input data
    dict_inputs = {
        "param": param,
        "infile": infile,
    }

    # Create process
    process = SecondProc(
        dict_inputs=dict_inputs,
        set_inputs=True,
    )

    # Define output paths
    process.output_paths["outfolder"] = outfolder

    # Run process
    process()
    process.finalize()