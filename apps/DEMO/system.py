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
    studies:list = None,
):
    # ---------------- #
    # Define processes #
    # ---------------- #
    processes = [
        {
            "process": Process1,
            "userParams": [
                "param1",
                "param2",
            ],
            "hardParams": {
                "hidden": 7,
            },
            "verbose": True,
            "execute": True,
        },
        {
            "process": Process2,
            "userParams": [
                "param3"
            ],
            "verbose": True,
            "execute": True,
        },
        {
            "process": Process3,
            "userParams": [
                "param2",
                "param4",
                "param5",
            ],
            "verbose": True,
            "execute": True,
        },
        {
            "process": Process4,
            "userParams": [
                "param3",
                "param6",
            ],
            "verbose": True,
            "execute": True,
        },
    ]
    
    # ------------------ #
    # Launch application #
    # ------------------ #
    app = nrs.Application(
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
        "Study1",
        # "Study2",
    ]

    main(
        working_dir=working_dir,
        studies=studies,
    )