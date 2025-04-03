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
    output3: str = attrs.field(init=False)
    output4: str = attrs.field(init=False)

    def __attrs_post_init__(self):
        super().__attrs_post_init__()

        self.require = [
            "output3",
            "output4",
        ]

    def __call__(self):
        super().__call__()

        self.subprocess9()
        self.subprocess10("output5.txt")

    def subprocess9(self):
        
        output = "I am the Sub-process 5.\n"
        output += "I belong to the Process 3.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param3 : {self.param3}\n"
        output += f"- param6 : {self.param6}\n"
        output += "\n"
        output += f"I know {self.require[0]} :\n"
        output += "\n"
        output += "'''\n"
        f = open(self.output3, "r")
        for line in f:
            output += "    " + line
        output += "\n'''\n"
        output += "\n"
        output += f"I know {self.require[1]} :\n"
        output += "\n"
        output += "'''\n"
        f = open(self.output4, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        print("---------------------------------------------------------")
        print(output)

    @nrs.Process.builder(
        build="output5",
    )
    def subprocess10(self,
        dump: str,
    ):
        
        output = "I am the Sub-process 6.\n"
        output += "I belong to the Process 3.\n"
        output += "\n"
        output += f"I am currently processing {self.index}.\n"
        output += "\n"
        output += "Here are the input parameters I know :\n"
        output += f"- param3 : {self.param3}\n"
        output += f"- param6 : {self.param6}\n"
        output += "\n"
        output += f"I know {self.require[0]} :\n"
        output += "\n"
        output += "'''\n"
        f = open(self.output3, "r")
        for line in f:
            output += "    " + line
        output += "\n'''\n"
        output += "\n"
        output += f"I know {self.require[1]} :\n"
        output += "\n"
        output += "'''\n"
        f = open(self.output4, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

        print("---------------------------------------------------------")
        print(output)

        with open(dump, "w") as f:
            f.write(output)


if __name__ == "__main__":

    # Name of the application using this item
    APP_NAME = os.path.split(__file__)[0].split("\\")[-2]

    # Define working directory
    cwd = Path(os.path.split(__file__)[0])
    working_dir = cwd / Path(f"../../../data/apps/{APP_NAME}")

    # Read input dataframe
    df_inputs = pd.read_excel(
        io=working_dir / "inputs.xlsx",
        index_col=0,
    )
    df_inputs.fillna(
        value="NA",
        inplace=True,
    )

    # Read paths dictionary
    with open(working_dir / "paths.json") as f:
        dict_paths = json.load(f)
    
    # Create process
    process = Process4(
        df_inputs=df_inputs,
        dict_paths=dict_paths,
        params=[
            "param3",
            "param6",
        ],
        erase=True,
        verbose=True,
    )

    # Select case
    process.index = "Test1"
    process.update_dict_params()
    
    # Go to working directory
    os.chdir(working_dir / f"4_Process4/{process.index}")

    # Launch process
    print(">>> START <<<")
    process()
    print(">>> COMPLETED <<<")