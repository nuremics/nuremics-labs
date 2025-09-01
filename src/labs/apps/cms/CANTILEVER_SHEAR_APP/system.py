import git
from pathlib import Path

from nuremics import Application
from labs.apps.cms.CANTILEVER_SHEAR_APP.procs import (
    GeometryProc,
)

APP_NAME = "CANTILEVER_SHEAR_APP"
repo = git.Repo(Path(__file__).resolve().parent, search_parent_directories=True)


def main():

    # --------------- #
    # Define workflow #
    # --------------- #
    workflow = [
        {
            "process": GeometryProc,
            "user_params": {
                "dim": "dimension",
            },
            "hard_params": {
                "length": 10.0,
                "width": 1.0,
                "height": 0.1,
            },
            "output_paths": {
                "outfile": "geometry",
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