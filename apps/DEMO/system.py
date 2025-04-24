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
    # ---------------- #
    # Define processes #
    # ---------------- #
    processes = [
        {
            "process": Process1,
            "input_params": [
                "param1",
                "param2",
            ],
            "input_paths": [
                "input1.txt",
            ],
        },
        {
            "process": Process2,
            "input_params": [
                "param3"
            ],
            "hard_params": {
                "hidden": 7,
            },
        },
        {
            "process": Process3,
            "input_params": [
                "param2",
                "param4",
                "param5",
            ],
        },
        {
            "process": Process4,
            "input_params": [
                "param3",
                "param6",
            ],
            "input_paths": [
                "input2.txt",
            ],
        },
    ]
    
    # ------------------ #
    # Launch application #
    # ------------------ #
    app = nrs.Application(
        app_name = APP_NAME,
        working_dir=working_dir,
        processes=processes,
        studies=studies,
    )
    app()


if __name__ == "__main__":
    
    # ------------------------ #
    # Define working directory #
    # ------------------------ #
    cwd = Path(os.path.split(__file__)[0])
    working_dir = cwd / Path(f"../../data/apps/{APP_NAME}")

    # -------------- #
    # Define studies #
    # -------------- #
    studies = [
        "Default",
        "Study1",
        # "Study2",
    ]

    main(
        working_dir=working_dir,
        # studies=studies,
    )