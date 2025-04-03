import os
from pathlib import Path

import nuremics as nrs

from items.item1 import Process1
from items.item2 import Process2
from items.item3 import Process3
from items.item4 import Process4

APP_NAME = os.path.split(__file__)[0].split("\\")[-1]

class Application:
    
    def __init__(
        self,
        working_dir: Path = None,
        erase: bool = True,
        verbose: bool = True,
    ):
        
        # ---------------------------- #
        # Define workflow of processes #
        # ---------------------------- #
        processes = [
            {
                "process": Process1,
                "userParams": [
                    "param1",
                    "param2",
                ],
                "fixedParams": {
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
        
        # ---------------------- #
        # Define workflow object #
        # ---------------------- #
        self.workflow = nrs.WorkFlow(
            working_dir=working_dir,
            app_name=APP_NAME,
            processes=processes,
            erase=erase,
            verbose=verbose,
        )

    def __call__(self):
        
        # --------------- #
        # Launch workflow #
        # --------------- #
        self.workflow()


if __name__ == "__main__":
    
    # ------------------------ #
    # Define working directory #
    # ------------------------ #
    cwd = Path(os.path.split(__file__)[0])
    working_dir = cwd / Path(f"../../data/apps/{APP_NAME}")
    working_dir.mkdir(exist_ok=True, parents=True)
    
    # ------------------ #
    # Launch application #
    # ------------------ #
    app = Application(working_dir)
    app()