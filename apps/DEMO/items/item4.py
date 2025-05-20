import os
import attrs
import inspect
import json
from pathlib import Path

from nuremics import Process, find_git_root

@attrs.define
class Process4(Process):

    # Parameters
    parameter1: str = attrs.field(init=False, metadata={"input": True})
    parameter2: float = attrs.field(init=False, metadata={"input": True})
    
    # Paths
    path1: Path = attrs.field(init=False, metadata={"input": True}, converter=Path)
    path2: Path = attrs.field(init=False, metadata={"input": True}, converter=Path)
    path3: Path = attrs.field(init=False, metadata={"input": True}, converter=Path)

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
        with open(self.path1) as f:
            content_path1 = f.read()
        with open(self.path2) as f:
            content_path2 = f.read()
        with open(self.path3) as f:
            content_path3 = f.read()
        
        # Set internal variable(s)
        self.variable = "Hello World!"

        # Do something
        something = f"({inspect.currentframe().f_code.co_name}) {"Play with it!"}"

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
        with open(self.path1) as f:
            content_path1 = f.read()
        with open(self.path2) as f:
            content_path2 = f.read()
        with open(self.path3) as f:
            content_path3 = f.read()
        
        # Set internal variable(s)
        self.variable = "Hello World!"

        # Do something
        something = f"({inspect.currentframe().f_code.co_name}) {"Play with it!"}"

        # Print some infos
        if self.verbose:
            print(something)

        # Define some results
        result = "Play with it!"

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
    git_dir = find_git_root()
    working_dir = git_dir / Path(f"data/apps/DEMO/Study1/4_Process4/Test1")

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
    process.output_paths["output1"] = "output5"

    # Launch process
    process()
    process.finalize()