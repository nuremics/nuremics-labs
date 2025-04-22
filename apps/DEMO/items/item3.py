import os
import attrs
import json
from pathlib import Path

import pandas as pd

import nuremics as nrs

@attrs.define
class Process3(nrs.Process):

    param2: float = attrs.field(init=False)
    param4: float = attrs.field(init=False)
    param5: float = attrs.field(init=False)
    output2: str = attrs.field(init=False)

    def __attrs_post_init__(self):

        self.require = [
            "output2",
        ]

    def __call__(self):
        super().__call__()

        self.subprocess5()
        self.subprocess6("output3.txt")
        self.subprocess7()
        self.subprocess8("output4.txt")

    def subprocess5(self):
        
        output = "I am the Sub-process 5.\n"
        output += "I belong to the Process 3.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param2 : {self.param2}\n"
        output += f"- param4 : {self.param4}\n"
        output += f"- param5 : {self.param5}\n"
        output += "\n"
        output += f"I know {self.require[0]} :\n"
        output += "\n"
        output += "'''\n"
        f = open(self.output2, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)

    @nrs.Process.builder(
        build="output3",
    )
    def subprocess6(self,
        dump: str,
    ):
        
        output = "I am the Sub-process 6.\n"
        output += "I belong to the Process 3.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param2 : {self.param2}\n"
        output += f"- param4 : {self.param4}\n"
        output += f"- param5 : {self.param5}\n"
        output += "\n"
        output += f"I know {self.require[0]} :\n"
        output += "\n"
        output += "'''\n"
        f = open(self.output2, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)

        with open(dump, "w") as f:
            f.write(output)

    def subprocess7(self):
        
        output = "I am the Sub-process 7.\n"
        output += "I belong to the Process 3.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param2 : {self.param2}\n"
        output += f"- param4 : {self.param4}\n"
        output += f"- param5 : {self.param5}\n"
        output += "\n"
        output += f"I know {self.require[0]} :\n"
        output += "\n"
        output += "'''\n"
        f = open(self.output2, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)

    @nrs.Process.builder(
        build="output4",
    )
    def subprocess8(self,
        dump: str,
    ):
        
        output = "I am the Sub-process 8.\n"
        output += "I belong to the Process 3.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param2 : {self.param2}\n"
        output += f"- param4 : {self.param4}\n"
        output += f"- param5 : {self.param5}\n"
        output += "\n"
        output += f"I know {self.require[0]} :\n"
        output += "\n"
        output += "'''\n"
        f = open(self.output2, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)
            print("---------------------------------------------------------")

        with open(dump, "w") as f:
            f.write(output)


if __name__ == "__main__":

    # Define working directory
    cwd = Path(os.path.split(__file__)[0])
    working_dir = cwd / Path(f"../../../data/apps/DEMO/Study1/3_Process3/Test1")

    # Go to working directory
    os.chdir(working_dir)

    # Read json containing parameters
    with open("parameters.json") as f:
        dict_params = json.load(f)
    
    # Create process
    process = Process3(
        dict_params=dict_params
    )

    # Launch process
    process()
    process.finalize()