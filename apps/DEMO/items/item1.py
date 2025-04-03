import os
import attrs
import json
from pathlib import Path

import pandas as pd

import nuremics as nrs

@attrs.define
class Process1(nrs.Process):

    param1: float = attrs.field(init=False)
    param2: float = attrs.field(init=False)
    hidden: int = attrs.field(init=False)

    def __attrs_post_init__(self):
        super().__attrs_post_init__()

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
    process = Process1(
        df_inputs=df_inputs,
        dict_paths=dict_paths,
        params=[
            "param1",
            "param2",
        ],
        dict_fixed_params={
            "hidden": 7,
        },
        erase=True,
        verbose=True,
    )

    # Select case
    process.index = "Test1"
    process.update_dict_params()
    
    # Go to working directory
    os.chdir(working_dir / f"1_Process1/{process.index}")

    # Launch process
    print(">>> START <<<")
    process()
    print(">>> COMPLETED <<<")