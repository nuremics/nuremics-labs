import os
from pathlib import Path
from nuremics import Application
from procs.OneProc.item import OneProc
from procs.AnotherProc.item import AnotherProc
from procs.AnalysisProc.item import AnalysisProc

APP_NAME = "ONE_APP"


def main(
    working_dir: Path | None = None,
    studies: list = ["Default"],
):
    # --------------- #
    # Define workflow #
    # --------------- #
    workflow = [
        {
            "process": OneProc,
            "user_params": {
                "param2": "parameter1",
            },
            "hard_params": {
                "param1": 0.5,
            },
            "user_paths": {
                "path1": "input1.txt",
            },
            "output_paths": {
                "out1": "output1.csv",
                "out2": "output2.png",
            },
        },
        {
            "process": AnotherProc,
            "user_params": {
                "param1": "parameter2",
                "param2": "parameter3",
            },
            "user_paths": {
                "path1": "input2.json",
                "path2": "input3",
            },
            "required_paths": {
                "path3": "output1.csv",
            },
            "output_paths": {
                "out1": "output3",
            },
        },
        {
            "process": AnalysisProc,
            "overall_analysis": {
                "analysis1": "output3",
            },
            "output_paths": {
                "out1": "output4.png",
            },
        },
    ]

    # ------------------ #
    # Define application #
    # ------------------ #
    app = Application(
        app_name=APP_NAME,
        working_dir=working_dir,
        workflow=workflow,
        studies=studies,
    )
    # Run it!
    app()


if __name__ == "__main__":

    # ------------------------ #
    # Define working directory #
    # ------------------------ #
    working_dir = Path(os.environ["WORKING_DIR"])

    # -------------- #
    # Define studies #
    # -------------- #
    studies = [
        "Study1",
        "Study2",
    ]

    # --------------- #
    # Run application #
    # --------------- #
    main(
        working_dir=working_dir,
        studies=studies,
    )
