from typing import Optional
from nuremics import Application
from nuremics_labs.procs.general.PolygonGeometryProc import PolygonGeometryProc
from nuremics_labs.procs.general.ProjectileModelProc import ProjectileModelProc
from nuremics_labs.procs.general.TrajectoryAnalysisProc import TrajectoryAnalysisProc


APP_NAME = "DEMO_APP"


def main(
    stage: Optional[str] = "run",
):

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

    # ----------------------------------- #
    # Define default values of parameters #
    # ----------------------------------- #
    default_params = {
        "nb_sides": 5,
        "gravity": -9.81,
        "mass": 0.1,
    }

    # ------------------ #
    # Define application #
    # ------------------ #
    app = Application(
        app_name=APP_NAME,
        workflow=workflow,
    )
    if stage == "config":
        app.configure()
    elif stage == "settings":
        app.configure()
        app.settings()
    elif stage == "run":
        app.configure()
        app.settings()
        app()
    
    return workflow, app, default_params


if __name__ == "__main__":

    # --------------- #
    # Run application #
    # --------------- #
    workflow, app = main(stage="run")