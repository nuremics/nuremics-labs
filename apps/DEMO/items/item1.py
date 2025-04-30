import os
import attrs
import json
from pathlib import Path

import nuremics as nrs

@attrs.define
class Process1(nrs.Process):

    param1: float = attrs.field(init=False)
    param2: float = attrs.field(init=False)
    input1: str = attrs.field(init=False)

    def __call__(self):
        super().__call__()

        self.operation1()
        self.operation2()
        self.operation3()

    def operation1(self):
        
        output = "I am the Sub-process 1.\n"
        output += "I belong to the Process 1.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param1 : {self.param1}\n"
        output += f"- param2 : {self.param2}\n"
        output += "\n"
        output += "Here is the input file I know :\n"
        output += f"- input1 : {self.input1}\n"
        output += "\n"
        output += "Whose the content is :\n"
        output += "'''\n"
        f = open(self.input1, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"
        output += "\n"
        output += "\n"
        output += "I don't know any output from previous processes."

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)

    def operation2(self):
        
        output = "I am the Sub-process 2.\n"
        output += "I belong to the Process 1.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param1 : {self.param1}\n"
        output += f"- param2 : {self.param2}\n"
        output += "\n"
        output += "Here is the input file I know :\n"
        output += f"- input1 : {self.input1}\n"
        output += "\n"
        output += "Whose the content is :\n"
        output += "'''\n"
        f = open(self.input1, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"
        output += "\n"
        output += "\n"
        output += "I don't know any output from previous processes."

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)

    def operation3(self):
        
        output = "I am the Sub-process 3.\n"
        output += "I belong to the Process 1.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param1 : {self.param1}\n"
        output += f"- param2 : {self.param2}\n"
        output += "\n"
        output += "Here is the input file I know :\n"
        output += f"- input1 : {self.input1}\n"
        output += "\n"
        output += "Whose the content is :\n"
        output += "'''\n"
        f = open(self.input1, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"
        output += "\n"
        output += "\n"
        output += "I don't know any output from previous processes."

        if self.verbose:
            print("---------------------------------------------------------")
            print(output)
            print("---------------------------------------------------------")

        dump = "output1.txt"
        with open(dump, "w") as f:
            f.write(output)
        
        self.update(
            build="output1",
            dump=dump,
        )


if __name__ == "__main__":
    
    # Define working directory
    cwd = Path(os.path.split(__file__)[0])
    working_dir = cwd / Path(f"../../../data/apps/DEMO/Default/1_Process1")

    # Go to working directory
    os.chdir(working_dir)

    # Read json containing parameters
    with open("parameters.json") as f:
        dict_params = json.load(f)
    
    # Create process
    process = Process1(
        dict_params=dict_params,
        from_inputs_json=True,
    )

    # Launch process
    process()
    process.finalize()