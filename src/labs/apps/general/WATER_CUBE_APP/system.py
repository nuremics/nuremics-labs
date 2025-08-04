import git
from pathlib import Path

from nuremics import Application
from labs.apps.general.WATER_CUBE_APP.procs.WaterCubeProc.item import WaterCubeProc

APP_NAME = "WATER_CUBE_APP"
repo = git.Repo(Path(__file__).resolve().parent, search_parent_directories=True)


def main():

    # --------------- #
    # Define workflow #
    # --------------- #
    workflow = [
        {
            "process": WaterCubeProc,
            # "user_params": {
            #     "n_sides": "nb_sides",
            # },
            # "hard_params": {
            #     "radius": 0.5,
            # },
            # "user_paths": {
            #     "title_file": "plot_title.txt",
            # },
            # "output_paths": {
            #     "coords_file": "points_coordinates.csv",
            #     "fig_file": "polygon_shape.png",
            # },
        }
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