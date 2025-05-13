import os
import attrs
import json
from pathlib import Path

import nuremics as nrs

@attrs.define
class Process1(nrs.Process):

    proc1_param1: float = attrs.field(init=False)
    proc1_param2: float = attrs.field(init=False)
    proc1_param3: float = attrs.field(init=False)
    proc1_input1: Path = attrs.field(init=False)

    def __call__(self):
        super().__call__()

        self.proc1_operation1()
        self.proc1_operation2()
        self.proc1_operation3()

    def proc1_operation1(self):
        
        output = "I am the proc1_operation1 function.\n"
        output += "I belong to the Process1 class.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- proc1_param1 : {self.proc1_param1}\n"
        output += f"- proc1_param2 : {self.proc1_param2}\n"
        output += f"- proc1_param3 : {self.proc1_param3}\n"
        output += "\n"
        output += "Here is the input path I know :\n"
        output += f"- proc1_input1 : {self.proc1_input1}\n"
        output += "\n"
        output += "The content of proc1_input1 is :\n"
        output += "'''\n"
        f = open(self.proc1_input1, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)

    def proc1_operation2(self):
        
        output = "I am the proc1_operation2 function.\n"
        output += "I belong to the Process1 class.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- proc1_param1 : {self.proc1_param1}\n"
        output += f"- proc1_param2 : {self.proc1_param2}\n"
        output += f"- proc1_param3 : {self.proc1_param3}\n"
        output += "\n"
        output += "Here is the input path I know :\n"
        output += f"- proc1_input1 : {self.proc1_input1}\n"
        output += "\n"
        output += "The content of proc1_input1 is :\n"
        output += "'''\n"
        f = open(self.proc1_input1, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)

    def proc1_operation3(self):
        
        output = "I am the proc1_operation3 function.\n"
        output += "I belong to the Process1 class.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- proc1_param1 : {self.proc1_param1}\n"
        output += f"- proc1_param2 : {self.proc1_param2}\n"
        output += f"- proc1_param3 : {self.proc1_param3}\n"
        output += "\n"
        output += "Here is the input path I know :\n"
        output += f"- proc1_input1 : {self.proc1_input1}\n"
        output += "\n"
        output += "The content of proc1_input1 is :\n"
        output += "'''\n"
        f = open(self.proc1_input1, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)
            print("---------------------------------------------------------")

        file = self.build["proc1_output1"]
        with open(file, "w") as f:
            f.write(output)


if __name__ == "__main__":
    
    # Define working directory
    cwd = Path(os.path.split(__file__)[0])
    working_dir = cwd / Path(f"../../../data/apps/DEMO/Study1/1_Process1/Test1")

    # Go to working directory
    os.chdir(working_dir)

    # Read json containing parameters
    with open("parameters.json") as f:
        dict_params = json.load(f)
    
    # Create process
    process = Process1(
        dict_params=dict_params,
        from_inputs_json=True,
        verbose=True,
    )
    process.build["proc1_output1"] = "output1.txt"

    # Launch process
    process()
    process.finalize()