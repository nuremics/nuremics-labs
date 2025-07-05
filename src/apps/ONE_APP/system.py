import sys
from pathlib import Path
import json
from nuremics import Application
from tkinter import Tk, filedialog
from procs.OneProc.item import OneProc
from procs.AnotherProc.item import AnotherProc
from procs.AnalysisProc.item import AnalysisProc

APP_NAME = "ONE_APP"


def main():

    # ---------------------------------------------------- #
    # Get (or ask) working directory from settings.json #
    # ---------------------------------------------------- #
    settings_path = Path(__file__).parent / "settings.json"
    with settings_path.open("r", encoding="utf-8") as f:
        settings = json.load(f)

    working_dir = settings.get("working_dir")

    # if working_dir == null
    if settings["working_dir"] is None:
        root = Tk()
        root.withdraw()  # Cache la fenêtre principale
        working_dir = filedialog.askdirectory(
            title=f"Chose working directory for {APP_NAME}"
        )
        if not working_dir:
            sys.exit(1)
        else:
            settings["working_dir"] = working_dir
            with settings_path.open("w", encoding="utf-8") as f:
                json.dump(settings, f, indent=2, ensure_ascii=False)

    working_dir = Path(working_dir)

    # -------------- #
    # Define studies #
    # -------------- #
    studies = [
        "Study1",
        "Study2",
    ]

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

    main()
