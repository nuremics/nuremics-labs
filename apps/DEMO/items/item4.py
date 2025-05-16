import os
import attrs
import json
from pathlib import Path

import nuremics as nrs

@attrs.define
class Process4(nrs.Process):

    # Parameters
    proc4_param1: str = attrs.field(init=False, metadata={"input": True})
    proc4_param2: float = attrs.field(init=False, metadata={"input": True})
    
    # Paths
    proc4_path1: Path = attrs.field(init=False, metadata={"input": True})
    proc4_path2: Path = attrs.field(init=False, metadata={"input": True})
    proc4_path3: Path = attrs.field(init=False, metadata={"input": True})

    def __call__(self):
        super().__call__()

        self.proc4_operation1()
        self.proc4_operation2()

    def proc4_operation1(self):
        
        output = "I am the proc4_operation1 function.\n"
        output += "I belong to the Process4 class.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- proc4_param1 : {self.proc4_param1}\n"
        output += f"- proc4_param2 : {self.proc4_param2}\n"
        output += "\n"
        output += "Here are the input paths I know :\n"
        output += f"- proc4_path1 : {self.proc4_path1}\n"
        output += f"- proc4_path2 : {self.proc4_path2}\n"
        output += f"- proc4_path3 : {self.proc4_path3}\n"
        output += "\n"
        output += "The content of proc4_path1 is :\n"
        output += "'''\n"
        f = open(self.proc4_path1, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"
        output += "\n"
        output += "\n"
        output += "The content of proc4_path2 is :\n"
        output += "'''\n"
        f = open(self.proc4_path2, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"
        output += "\n"
        output += "\n"
        output += "The content of proc4_path3 is :\n"
        output += "'''\n"
        f = open(self.proc4_path3, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)

    def proc4_operation2(self):
        
        output = "I am the proc4_operation2 function.\n"
        output += "I belong to the Process4 class.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- proc4_param1 : {self.proc4_param1}\n"
        output += f"- proc4_param2 : {self.proc4_param2}\n"
        output += "\n"
        output += "Here are the input paths I know :\n"
        output += f"- proc4_path1 : {self.proc4_path1}\n"
        output += f"- proc4_path2 : {self.proc4_path2}\n"
        output += f"- proc4_path3 : {self.proc4_path3}\n"
        output += "\n"
        output += "The content of proc4_path1 is :\n"
        output += "'''\n"
        f = open(self.proc4_path1, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"
        output += "\n"
        output += "\n"
        output += "The content of proc4_path2 is :\n"
        output += "'''\n"
        f = open(self.proc4_path2, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"
        output += "\n"
        output += "\n"
        output += "The content of proc4_path3 is :\n"
        output += "'''\n"
        f = open(self.proc4_path3, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)

        file = self.build["proc4_output1"]
        with open(file, "w") as f:
            f.write(output)


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