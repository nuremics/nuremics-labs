import os
from pathlib import Path

import nuremics as nrs

APP_NAME = "DEMO"

from items.item1 import Process1
from items.item2 import Process2
from items.item3 import Process3
from items.item4 import Process4

def main(
    working_dir:Path = None,
    studies:list = ["Default"],
):
    # --------------- #
    # Define workflow #
    # --------------- #
    workflow = [
        {
            "process": Process1,
            "user_params": {
                "proc1_param1": "param1", 
                "proc1_param2": "param2", 
                "proc1_param3": "param3",
            },
            "user_paths": {
                "proc1_path1": "input1.txt",
            },
            "build": {
                "proc1_output1": "output1.txt",
            },
        },
        {
            "process": Process2,
            "hard_params": {
                "proc2_param1": 0.887, 
            },
            "user_paths": {
                "proc2_path1": "input1.txt",
                "proc2_path2": "input2.txt",
            },
            "require":{
                "proc2_path3": "output1.txt",
            },
            "build": {
                "proc2_output1": "output2.txt",
            },
        },
        {
            "process": Process3,
            "user_params": {
                "proc3_param1": "param2",
                "proc3_param2": "param4",
                "proc3_param3": "param5",
            },
            "require":{
                "proc3_path1": "output2.txt",
            },
            "build": {
                "proc3_output1": "output3.txt",
                "proc3_output2": "output4.txt",
            },
        },
        {
            "process": Process4,
            "user_params": {
                "proc4_param1": "param3",
                "proc4_param2": "param6",
            },
            "user_paths": {
                "proc4_path1": "input3.txt",
            },
            "require":{
                "proc4_path2": "output3.txt",
                "proc4_path3": "output4.txt",
            },
            "build": {
                "proc4_output1": "output5.txt",
            },
        },
    ]
    
    # ------------------ #
    # Launch application #
    # ------------------ #
    app = nrs.Application(
        app_name=APP_NAME,
        working_dir=working_dir,
        workflow=workflow,
        studies=studies,
    )
    app()


if __name__ == "__main__":
    
    # ------------------------ #
    # Define working directory #
    # ------------------------ #
    cwd = Path(os.path.split(__file__)[0])
    working_dir = cwd / Path(f"../../data/apps")

    # -------------- #
    # Define studies #
    # -------------- #
    studies = [
        "Study1",
        # "Study2",
    ]

    main(
        working_dir=working_dir,
        studies=studies,
    )