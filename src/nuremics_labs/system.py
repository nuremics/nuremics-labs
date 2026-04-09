import sys
from pathlib import Path
from typing import Optional

from nuremics import Application

import nuremics_labs

APPS_DIR = Path(nuremics_labs.__file__).parent


def main(
    app_id: list,
    stage: Optional[str] = "run",
) -> None:

    # ------------------ #
    # Define application #
    # ------------------ #
    app = Application(
        app_id=app_id,
        apps_dir=APPS_DIR,
        stage=stage,
    )
    app()
    
    return app.list_workflow, app, app.default_params


if __name__ == "__main__":

    # --------------- #
    # Run application #
    # --------------- #
    workflow, app, _ = main(
        app_id=[sys.argv[1], sys.argv[2]],
        stage="run",
    )