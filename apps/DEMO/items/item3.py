import os
import attrs
import inspect
import json
from pathlib import Path

from nuremics import Process

@attrs.define
class Process3(Process):

    # Parameters
    parameter1: int = attrs.field(init=False, metadata={"input": True})
    parameter2: float = attrs.field(init=False, metadata={"input": True})
    parameter3: bool = attrs.field(init=False, metadata={"input": True})

    # Paths
    path1: Path = attrs.field(init=False, metadata={"input": True})

    # Internal
    variable: bool = attrs.field(init=False)

    def __call__(self):
        super().__call__()

        self.operation1()
        self.operation2()
        self.operation3()
        self.operation4()

    def operation1(self):
        
        # Useful attributes from the parent class Process
        self.study
        if self.is_case:
            self.index
        
        # Accessible input parameter(s)
        self.parameter1
        self.parameter2
        self.parameter3
        
        # Accessible input path(s)
        self.path1
        
        # Set internal variable(s)
        self.variable = True

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
        self.parameter3
        
        # Accessible input path(s)
        self.path1
        
        # Accessible internal variable(s)
        self.variable

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

    def operation3(self):
        
        # Useful attributes from the parent class Process
        self.study
        if self.is_case:
            self.index
        
        # Accessible input parameter(s)
        self.parameter1
        self.parameter2
        self.parameter3
        
        # Accessible input path(s)
        self.path1
        
        # Accessible internal variable(s)
        self.variable

        # Play with it!
        something = f"({inspect.currentframe().f_code.co_name}) "
        something += "..."

        # Print some infos
        if self.verbose:
            print(something)

    def operation4(self):
        
        # Useful attributes from the parent class Process
        self.study
        if self.is_case:
            self.index
        
        # Accessible input parameter(s)
        self.parameter1
        self.parameter2
        self.parameter3
        
        # Accessible input path(s)
        self.path1
        
        # Accessible internal variable(s)
        self.variable

        # Play with it!
        something = f"({inspect.currentframe().f_code.co_name}) "
        something += "..."

        # Print some infos
        if self.verbose:
            print(something)

        # Play with it!
        result = "..."

        # Write some results in output file or directory
        file = self.output_paths["output2"]
        with open(file, "w") as f:
            f.write(result)


if __name__ == "__main__":

    # Define working directory
    cwd = Path(os.path.split(__file__)[0])
    working_dir = cwd / Path(f"../../../data/apps/DEMO/Study1/3_Process3/Test1")

    # Go to working directory
    os.chdir(working_dir)

    # Read json containing parameters
    with open("inputs.json") as f:
        dict_inputs = json.load(f)
    
    # Create process
    process = Process3(
        dict_inputs=dict_inputs,
        set_inputs=True,
        verbose=True,
    )
    process.build["proc3_output1"] = "output3.txt"
    process.build["proc3_output2"] = "output4.txt"

    # Launch process
    process()
    process.finalize()