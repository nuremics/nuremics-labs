
import git
from pathlib import Path

from nuremics import Application
from labs.procs.general.PolygonGeometryProc.item import PolygonGeometryProc
from labs.procs.general.ProjectileModelProc.item import ProjectileModelProc
from labs.procs.general.TrajectoryAnalysisProc.item import TrajectoryAnalysisProc

APP_NAME = "DEMO_APP"
repo = git.Repo(Path(__file__).resolve().parent, search_parent_directories=True)

def main():

    # --------------- #
    # Define workflow #
    # --------------- #
    workflow = [
        {
            "process": PolygonGeometryProc,
            "user_params": {
                "n_sides": "nb_sides",
            },
            "hard_params": {
                "radius": 0.5,
            },
            "user_paths": {
                "title_file": "plot_title.txt",
            },
            "output_paths": {
                "coords_file": "points_coordinates.csv",
                "fig_file": "polygon_shape.png",
            },
        },
        {
            "process": ProjectileModelProc,
            "user_params": {
                "gravity": "gravity",
                "mass": "mass",
            },
            "user_paths": {
                "velocity_file": "velocity.json",
                "configs_folder": "configs",
            },
            "required_paths": {
                "coords_file": "points_coordinates.csv",
            },
            "output_paths": {
                "comp_folder": "comparison",
            },
        },
        {
            "process": TrajectoryAnalysisProc,
            "overall_analysis": {
                "comp_folder": "comparison",
            },
            "output_paths": {
                "fig_file": "overall_comparisons.png",
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