import os
import attrs
import inspect
import json
from pathlib import Path

from nuremics import Process

@attrs.define
class Process2(Process):

    # Parameters
    parameter1: float = attrs.field(init=False, metadata={"input": True})

    # Paths
    path1: Path = attrs.field(init=False, metadata={"input": True})
    path2: Path = attrs.field(init=False, metadata={"input": True})
    path3: Path = attrs.field(init=False, metadata={"input": True})

    # Internal
    variable: int = attrs.field(init=False)

    def __call__(self):
        super().__call__()

        self.operation1()

    def operation1(self):
        
        # Useful attributes from the parent class Process
        self.study
        if self.is_case:
            self.index
        
        # Accessible input parameter(s)
        self.parameter1
        
        # Accessible input path(s)
        self.path1
        self.path2
        self.path3
        
        # Set internal variable(s)
        self.variable = 14 

        # Play with it!
        something = f"({inspect.currentframe().f_code.co_name}) "
        something += "..."

        # Print some infos
        if self.verbose:
            print(something)

        # Play with it!
        result = "..."

        # Write some results in output file or directory
        file = self.output_paths["output1"]
        with open(file, "w") as f:
            f.write(result)


if __name__ == "__main__":

    # Define working directory
    cwd = Path(os.path.split(__file__)[0])
    working_dir = cwd / Path(f"../../../data/apps/DEMO/Study1/2_Process2")

    # Go to working directory
    os.chdir(working_dir)

    # Read json containing parameters
    with open("inputs.json") as f:
        dict_inputs = json.load(f)
    
    # Create process
    process = Process2(
        dict_inputs=dict_inputs,
        set_inputs=True,
        verbose=True,
    )
    process.output_paths["output1"] = "output2.txt"

    # Launch process
    process()
    process.finalize()