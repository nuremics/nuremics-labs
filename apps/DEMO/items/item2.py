import os
import attrs
import json
from pathlib import Path

import nuremics as nrs

@attrs.define
class Process2(nrs.Process):

    param3: float = attrs.field(init=False)
    hidden: int = attrs.field(init=False)
    output1: str = attrs.field(init=False)

    def __attrs_post_init__(self):

        self.require = [
            "output1",
        ]

    def __call__(self):
        super().__call__()

        self.subprocess4("output2.txt")

    @nrs.Process.builder(
        build="output2",
    )
    def subprocess4(self,
        dump: str,
    ):
        
        output = "I am the Sub-process 4.\n"
        output += "I belong to the Process 2.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param3 : {self.param3}\n"
        output += f"- hidden : {self.hidden}\n"
        output += "\n"
        output += f"I know {self.require[0]} :\n"
        output += "\n"
        output += "'''\n"
        f = open(self.output1, "r")
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
    working_dir = cwd / Path(f"../../../data/apps/DEMO/Study1/2_Process2/Test1")

    # Go to working directory
    os.chdir(working_dir)

    # Read json containing parameters
    with open("parameters.json") as f:
        dict_params = json.load(f)
    
    # Create process
    process = Process2(
        dict_params=dict_params
    )

    # Launch process
    process()
    process.finalize()