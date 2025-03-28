import os
from pathlib import Path

import nuremics as nrs

import items.item1 as item1
import items.item2 as item2
import items.item3 as item3
import items.item4 as item4

APP_NAME = os.path.split(__file__)[0].split("\\")[-1]

class Application:
    
    def __init__(
        self,
        working_dir: Path = None,
        verbose: bool = True,
    ):
        
        # ---------------------------- #
        # Define workflow of processes #
        # ---------------------------- #
        processes = [
            {
                "module": item1.Process1,
                "userParams": item1.userParams,
                "verbose": True,
                "execute": True,
            },
            {
                "module": item2.Process2,
                "userParams": item2.userParams,
                "verbose": True,
                "execute": True,
            },
            {
                "module": item3.Process3,
                "userParams": item3.userParams,
                "verbose": True,
                "execute": True,
            },
            {
                "module": item4.Process4,
                "userParams": item4.userParams,
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