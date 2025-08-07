import os
import attrs
from pathlib import Path

from nuremics import Process
from labs.apps.general.BASE_APP.procs.FirstProc.ops import (
    operation,
)


@attrs.define
class FirstProc(Process):
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
        param : float
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
        outfile : txt
            Description of the file.
    """

    # Parameters
    param: float = attrs.field(init=False, metadata={"input": True})

    # Paths
    # infile: Path = attrs.field(init=False, metadata={"input": True}, converter=Path)

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
            outfile
        """

        # with open(self.infile) as file:
        #     content = file.read()

        self.variable = operation(
            param=self.param,
            outfile=self.output_paths["outfile"],
            # content=content,
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
    param = 1.4

    # Input paths
    infile = Path(r"...") / "input.txt"

    # Output paths
    outfile = "output.txt"

    # ================================================================== #

    # Go to working directory
    os.chdir(working_dir)

    # Create dictionary containing input data
    dict_inputs = {
        "param": param,
        "infile": infile,
    }

    # Create process
    process = FirstProc(
        dict_inputs=dict_inputs,
        set_inputs=True,
    )

    # Define output paths
    process.output_paths["outfile"] = outfile

    # Run process
    process()
    process.finalize()