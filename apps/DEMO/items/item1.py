import os
import attrs
import json
from pathlib import Path

import nuremics as nrs

@attrs.define
class Process1(nrs.Process):

    param1: float = attrs.field(init=False)
    param2: float = attrs.field(init=False)
    hidden: int = attrs.field(init=False)

    def __attrs_post_init__(self):

        self.require = []

    def __call__(self):
        super().__call__()

        self.subprocess1()
        self.subprocess2()
        self.subprocess3("output1.txt")

    def subprocess1(self):
        
        output = "I am the Sub-process 1.\n"
        output += "I belong to the Process 1.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param1 : {self.param1}\n"
        output += f"- param2 : {self.param2}\n"
        output += f"- hidden : {self.hidden}\n"
        output += "\n"
        output += "I don't know any output from previous processes."

        print("---------------------------------------------------------")
        print(output)

    def subprocess2(self):
        
        output = "I am the Sub-process 2.\n"
        output += "I belong to the Process 1.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param1 : {self.param1}\n"
        output += f"- param2 : {self.param2}\n"
        output += f"- hidden : {self.hidden}\n"
        output += "\n"
        output += "I don't know any output from previous processes."

        print("---------------------------------------------------------")
        print(output)

    @nrs.Process.builder(
        build="output1",
    )
    def subprocess3(self,
        dump: str,
    ):
        
        output = "I am the Sub-process 3.\n"
        output += "I belong to the Process 1.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param1 : {self.param1}\n"
        output += f"- param2 : {self.param2}\n"
        output += f"- hidden : {self.hidden}\n"
        output += "\n"
        output += "I don't know any output from previous processes."

        print("---------------------------------------------------------")
        print(output)
        print("---------------------------------------------------------")

        with open(dump, "w") as f:
            f.write(output)


if __name__ == "__main__":
    
    # Define working directory
    cwd = Path(os.path.split(__file__)[0])
    working_dir = cwd / Path(f"../../../data/apps/DEMO/Study1/1_Process1")

    # Go to working directory
    os.chdir(working_dir)

    # Read json containing parameters
    with open("parameters.json") as f:
        dict_params = json.load(f)
    
    # Create process
    process = Process1(
        dict_params=dict_params
    )

    # Launch process
    process()
    process.finalize()