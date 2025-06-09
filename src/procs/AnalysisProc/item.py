import os
import attrs
import json
from pathlib import Path

from nuremics import Process
from procs.AnalysisProc import utils


@attrs.define
class AnalysisProc(Process):
    """
    Compare simulated (model) and theoretical trajectories of a projectile across all experiments. 

    Pipeline
    --------
        1. operation1
            Generate overall comparative plot of simulated (model) and theoritical trajectories.

    Analysis
    --------
        - analysis1 : folder
            'results.xlsx' : File containing model and theoritical trajectories.

    Outputs (stored in self.output_paths)
    -------
        out1 : png
            Image comparing both trajectories across all experiments.
    """

    # Analysis
    metadata = {
        "input": True,
        "analysis": True,
        "settings": {
            "add": True,
            "line": "--r",
            "label": "Model"
        }
    }
    analysis1: str = attrs.field(init=False, metadata=metadata)

    def __call__(self):
        super().__call__()

        self.operation1()
    
    def operation1(self):
        """
        Generate overall comparative plot of simulated (model) and theoritical trajectories.

        Uses
        ----
            analysis1

        Generates
        ---------
            out1
        """

        self.process_output(
            out=self.analysis1,
            func=utils.run_analysis,
            filename=self.output_paths["out1"],
            verbose=self.verbose,
        )


if __name__ == "__main__":
    
    # Define working directory
    working_dir = Path(os.environ["WORKING_DIR"])/"ONE_APP/Study1/3_AnalysisProc"

    # Go to working directory
    os.chdir(working_dir)

    # Create dictionary containing input data
    dict_inputs = {
        "analysis1": "output3",
    }
    
    # Create process
    process = AnalysisProc(
        dict_inputs=dict_inputs,
        set_inputs=True,
    )
    process.output_paths["out1"] = "output4.png"

    # Get dictionary of paths
    with open(working_dir/"../.paths.json") as f:
        process.dict_paths = json.load(f) 

    # Get dictionary of analysis settings
    with open(working_dir/"../analysis.json") as f:
        process.dict_analysis = json.load(f) 

    # Run process
    process()
    process.finalize()