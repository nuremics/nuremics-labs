import os
import attrs
import inspect
import json
from pathlib import Path

from nuremics import Process

@attrs.define
class Process4(Process):

    # Parameters
    parameter1: str = attrs.field(init=False, metadata={"input": True})
    parameter2: float = attrs.field(init=False, metadata={"input": True})
    
    # Paths
    path1: Path = attrs.field(init=False, metadata={"input": True})
    path2: Path = attrs.field(init=False, metadata={"input": True})
    path3: Path = attrs.field(init=False, metadata={"input": True})

    # Internal
    variable: str = attrs.field(init=False)

    def __call__(self):
        super().__call__()

        self.operation1()
        self.operation2()

    def operation1(self):
        
        # Useful attributes from the parent class Process
        self.study
        if self.is_case:
            self.index
        
        # Accessible input parameter(s)
        self.parameter1
        self.parameter2
        
        # Accessible input path(s)
        self.path1
        self.path2
        self.path3
        
        # Set internal variable(s)
        self.variable = "Hello World!"

        # Play with it!
        something = f"({inspect.currentframe().f_code.co_name}) "
        something += "..."

        # Print some infos
        if self.verbose:
            print(something)

    def operation2(self):
        
        # Useful attributes from the parent class Process
        self.study
        if self.is_case:
            self.index
        
        # Accessible input parameter(s)
        self.parameter1
        self.parameter2
        
        # Accessible input path(s)
        self.path1
        self.path2
        self.path3
        
        # Set internal variable(s)
        self.variable = "Hello World!"

        # Play with it!
        something = f"({inspect.currentframe().f_code.co_name}) "
        something += "..."

        # Print some infos
        if self.verbose:
            print(something)

        # Play with it!
        result = "..."

        # Write some results in output file or directory
        dir = Path(self.output_paths["output1"])
        dir.mkdir(
            exist_ok=True,
            parents=True,
        )
        file = "any_name.txt"
        with open(dir / file, "w") as f:
            f.write(result)


if __name__ == "__main__":

    # Define working directory
    cwd = Path(os.path.split(__file__)[0])
    working_dir = cwd / Path(f"../../../data/apps/DEMO/Study1/4_Process4/Test1")

    # Go to working directory
    os.chdir(working_dir)

    # Read json containing parameters
    with open("inputs.json") as f:
        dict_inputs = json.load(f)
    
    # Create process
    process = Process4(
        dict_inputs=dict_inputs,
        set_inputs=True,
        verbose=True,
    )
    process.build["proc4_output1"] = "output5.txt"

    # Launch process
    process()
    process.finalize()