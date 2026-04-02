import sys
from pathlib import Path
from typing import Optional

import yaml
from nuremics import Application

from nuremics_labs import registery

APP_DIR = Path("apps")
APP_REGISTRY = {
    f.stem: str(f) for f in APP_DIR.glob("**/*.yaml")
}


# def main(
#     app_file: Path,
#     stage: Optional[str] = "run",
# ) -> None:
    
#     # ------------- #
#     # Load App file #
#     # ------------- #
#     with open(app_file) as f:
#         dict_app = yaml.safe_load(f)
    
#     # --------------- #
#     # Define App name #
#     # --------------- #
#     app_name = dict_app["app_name"]

#     # --------------- #
#     # Define workflow #
#     # --------------- #
#     workflow = dict_app["workflow"]

#     # ----------------------------------- #
#     # Define default values of parameters #
#     # ----------------------------------- #
#     default_params = dict_app["default_params"]

#     # ------------------ #
#     # Define application #
#     # ------------------ #
#     app = Application(
#         app_name=app_name,
#         workflow=workflow,
#     )
#     if stage == "config":
#         app.configure()
#     elif stage == "settings":
#         app.configure()
#         app.settings()
#     elif stage == "run":
#         app.configure()
#         app.settings()
#         app()
    
#     return workflow, app, default_params


# if __name__ == "__main__":

#     # --------------- #
#     # Run application #
#     # --------------- #
#     workflow, app, _ = main(
#         app_file=Path(sys.argv[1]),
#         stage="run",
#     )