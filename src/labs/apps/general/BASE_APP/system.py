import git
from pathlib import Path

from nuremics import Application
from labs.apps.general.BASE_APP.procs import (
    FirstProc,
    SecondProc,
)

APP_NAME = "BASE_APP"
repo = git.Repo(Path(__file__).resolve().parent, search_parent_directories=True)


def main():

    # --------------- #
    # Define workflow #
    # --------------- #
    workflow = [
        {
            "process": FirstProc,
            "hard_params": {
                "param": 1.4,
            },
            # "user_paths": {
            #     "infile": "input.txt",
            # },
            "output_paths": {
                "outfile": "output.txt",
            },
        },
        {
            "process": SecondProc,
            # "user_params": {
            #     "param": "parameter",
            # },
            "required_paths": {
                "infile": "output.txt",
            },
            "output_paths": {
                "outfolder": "output",
            },
        },
    ]

    # ------------------ #
    # Define application #
    # ------------------ #
    app = Application(
        app_name=APP_NAME,
        nuremics_dir=repo.working_tree_dir,
        workflow=workflow,
    )
    # Run it!
    app()


if __name__ == "__main__":

    # --------------- #
    # Run application #
    # --------------- #
    main()