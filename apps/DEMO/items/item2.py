import os
import attrs
import json
from pathlib import Path

import pandas as pd

import nuremics as nrs

@attrs.define
class Process2(nrs.AllProcesses):

    param3: float = attrs.field(init=False)
    output1_path: str = attrs.field(init=False)

    def __attrs_post_init__(self):
        super().__attrs_post_init__()

        self.require = [
            "output1",
        ]

    def __call__(self):

        self.output1_path = self.get_build_path(self.require[0])

        for param in self.user_params:
            setattr(self, param, self.dict_params[param])
        for param in self.dict_fixed_params.keys():
            setattr(self, param, self.dict_fixed_params[param])

        self.subprocess4("output2.txt")

    @nrs.AllProcesses.builder(
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
        output += f"- Param3 : {self.param3}.\n"
        output += "\n"
        output += f"I know {self.require[0]} :\n"
        output += "\n"
        output += "'''\n"
        f = open(self.output1_path, "r")
        for line in f:
            output += "    " + line
        output += "\n'''"

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
    process = Process2(
        df_inputs=df_inputs,
        dict_paths=dict_paths,
        params=[
            "param3"
        ],
        verbose=True,
    )

    # Select case
    process.index = "Test1"
    process.update_dict_params()
    
    # Go to working directory
    os.chdir(working_dir / f"2_Process2/{process.index}")

    # Launch process
    print(">>> START <<<")
    process()
    print(">>> COMPLETED <<<")