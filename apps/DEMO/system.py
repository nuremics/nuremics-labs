import os
from pathlib import Path

from nuremics import Application

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
                "parameter1": "param1", 
                "parameter2": "param2", 
                "parameter3": "param3",
            },
            "user_paths": {
                "path1": "input1.txt",
            },
            "output_paths": {
                "output1": "output1.txt",
            },
        },
        {
            "process": Process2,
            "hard_params": {
                "parameter1": 0.887, 
            },
            "user_paths": {
                "path1": "input1.txt",
                "path2": "input2.txt",
            },
            "required_paths":{
                "path3": "output1.txt",
            },
            "output_paths": {
                "output1": "output2.txt",
            },
        },
        {
            "process": Process3,
            "user_params": {
                "parameter1": "param2",
                "parameter2": "param4",
                "parameter3": "param5",
            },
            "required_paths":{
                "path1": "output2.txt",
            },
            "output_paths": {
                "output1": "output3.txt",
                "output2": "output4.txt",
            },
        },
        {
            "process": Process4,
            "user_params": {
                "parameter1": "param3",
                "parameter2": "param6",
            },
            "user_paths": {
                "path1": "input3.txt",
            },
            "required_paths":{
                "path2": "output3.txt",
                "path3": "output4.txt",
            },
            "output_paths": {
                "output1": "output5",
            },
        },
    ]

    # ------------------ #
    # Launch application #
    # ------------------ #
    app = Application(
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
        "Study2",
    ]

    main(
        working_dir=working_dir,
        studies=studies,
    )