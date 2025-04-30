import os
import attrs
import json
from pathlib import Path

import pandas as pd

import nuremics as nrs

@attrs.define
class Process4(nrs.Process):

    param3: float = attrs.field(init=False)
    param6: float = attrs.field(init=False)
    input2: str = attrs.field(init=False)
    output3: str = attrs.field(init=False)
    output4: str = attrs.field(init=False)

    def __call__(self):
        super().__call__()

        self.operation9()
        self.operation10()

    def operation9(self):
        
        output = "I am the Sub-process 5.\n"
        output += "I belong to the Process 3.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param3 : {self.param3}\n"
        output += f"- param6 : {self.param6}\n"
        output += "\n"
        output += "Here is the input file I know :\n"
        output += f"- input2 : {self.input2}\n"
        output += "\n"
        output += "Whose the content is :\n"
        output += "'''\n"
        f = open(self.input2, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"
        output += "\n"
        output += "\n"
        output += f"I know output3 :\n"
        output += "\n"
        output += "'''\n"
        f = open(self.output3, "r")
        for line in f:
            output += "    " + line
        output += "\n'''\n"
        output += "\n"
        output += f"I know output4 :\n"
        output += "\n"
        output += "'''\n"
        f = open(self.output4, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)

    def operation10(self):
        
        output = "I am the Sub-process 6.\n"
        output += "I belong to the Process 3.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param3 : {self.param3}\n"
        output += f"- param6 : {self.param6}\n"
        output += "\n"
        output += "\n"
        output += "Here is the input file I know :\n"
        output += f"- input1 : {self.input2}\n"
        output += "\n"
        output += "Whose the content is :\n"
        output += "'''\n"
        f = open(self.input2, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"
        output += "\n"
        output += f"I know output3 :\n"
        output += "\n"
        output += "'''\n"
        f = open(self.output3, "r")
        for line in f:
            output += "    " + line
        output += "\n'''\n"
        output += "\n"
        output += f"I know output4 :\n"
        output += "\n"
        output += "'''\n"
        f = open(self.output4, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)

        dump = "output5.txt"
        with open(dump, "w") as f:
            f.write(output)
        
        self.update(
            build="output5",
            dump=dump,
        )


if __name__ == "__main__":

    # Define working directory
    cwd = Path(os.path.split(__file__)[0])
    working_dir = cwd / Path(f"../../../data/apps/DEMO/Default/4_Process4/Test1")

    # Go to working directory
    os.chdir(working_dir)

    # Read json containing parameters
    with open("parameters.json") as f:
        dict_params = json.load(f)
    
    # Create process
    process = Process4(
        dict_params=dict_params,
        from_inputs_json=True,
    )

    # Launch process
    process()
    process.finalize()