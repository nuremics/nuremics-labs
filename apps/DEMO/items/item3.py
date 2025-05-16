import os
import attrs
import json
from pathlib import Path

import nuremics as nrs

@attrs.define
class Process3(nrs.Process):

    # Parameters
    proc3_param1: int = attrs.field(init=False, metadata={"input": True})
    proc3_param2: float = attrs.field(init=False, metadata={"input": True})
    proc3_param3: bool = attrs.field(init=False, metadata={"input": True})

    # Paths
    proc3_path1: Path = attrs.field(init=False, metadata={"input": True})

    def __call__(self):
        super().__call__()

        self.proc3_operation1()
        self.proc3_operation2()
        self.proc3_operation3()
        self.proc3_operation4()

    def proc3_operation1(self):
        
        output = "I am the proc3_operation1 function.\n"
        output += "I belong to the Process3 class.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- proc3_param1 : {self.proc3_param1}\n"
        output += f"- proc3_param2 : {self.proc3_param2}\n"
        output += f"- proc3_param3 : {self.proc3_param3}\n"
        output += "\n"
        output += "Here is the input path I know :\n"
        output += f"- proc3_path1 : {self.proc3_path1}\n"
        output += "\n"
        output += "The content of proc3_path1 is :\n"
        output += "'''\n"
        f = open(self.proc3_path1, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)

    def proc3_operation2(self):
        
        output = "I am the proc3_operation2 function.\n"
        output += "I belong to the Process3 class.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- proc3_param1 : {self.proc3_param1}\n"
        output += f"- proc3_param2 : {self.proc3_param2}\n"
        output += f"- proc3_param3 : {self.proc3_param3}\n"
        output += "\n"
        output += "Here is the input path I know :\n"
        output += f"- proc3_path1 : {self.proc3_path1}\n"
        output += "\n"
        output += "The content of proc3_path1 is :\n"
        output += "'''\n"
        f = open(self.proc3_path1, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)

        file = self.build["proc3_output1"]
        with open(file, "w") as f:
            f.write(output)

    def proc3_operation3(self):
        
        output = "I am the proc3_operation3 function.\n"
        output += "I belong to the Process3 class.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- proc3_param1 : {self.proc3_param1}\n"
        output += f"- proc3_param2 : {self.proc3_param2}\n"
        output += f"- proc3_param3 : {self.proc3_param3}\n"
        output += "\n"
        output += "Here is the input path I know :\n"
        output += f"- proc3_path1 : {self.proc3_path1}\n"
        output += "\n"
        output += "The content of proc3_path1 is :\n"
        output += "'''\n"
        f = open(self.proc3_path1, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)

    def proc3_operation4(self):
        
        output = "I am the proc3_operation1 function.\n"
        output += "I belong to the Process3 class.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- proc3_param1 : {self.proc3_param1}\n"
        output += f"- proc3_param2 : {self.proc3_param2}\n"
        output += f"- proc3_param3 : {self.proc3_param3}\n"
        output += "\n"
        output += "Here is the input path I know :\n"
        output += f"- proc3_path1 : {self.proc3_path1}\n"
        output += "\n"
        output += "The content of proc3_path1 is :\n"
        output += "'''\n"
        f = open(self.proc3_path1, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)
            print("---------------------------------------------------------")
        
        file = self.build["proc3_output2"]
        with open(file, "w") as f:
            f.write(output)
        
        # file4 = self.build["proc3_output2qdazd"]


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