import os
import attrs
import json
from pathlib import Path

from nuremics import Process
from nuremics_labs.ops.general import trajectory_analysis


@attrs.define
class TrajectoryAnalysisProc(Process):
    """
    Perform overall comparisons between simulated (model) and theoretical trajectories.

    Pipeline
    --------
        A/ plot_overall_model_vs_theory
            Generate overall comparative plots of simulated (model) and theoritical trajectories.

    Analysis
    --------
        - comp_folder : folder
            'results.xlsx' : File containing both trajectories.

    Outputs (stored in self.output_paths)
    -------
        fig_file : png
            Image containing overall comparative plots.
    """

    # Analysis
    metadata = {
        "input": True,
        "analysis": True,
        "settings": {
            "add": True,
            "color": "red",
            "linestyle": "None",
            "linewidth": 2.0,
            "marker": "o",
            "markersize": 8,
            "markevery": 20,
            "label": ""
        }
    }
    comp_folder: str = attrs.field(init=False, metadata=metadata)

    def __call__(self):
        super().__call__()

        self.plot_overall_model_vs_theory()
    
    def plot_overall_model_vs_theory(self):
        """
        Generate overall comparative plots of simulated (model) and theoritical trajectories.

        Uses
        ----
            comp_folder

        Generates
        ---------
            fig_file
        """

        self.process_output(
            out=self.comp_folder,
            func=trajectory_analysis.plot_overall_model_vs_theory,
            filename=self.output_paths["fig_file"],
            silent=self.silent,
        )


if __name__ == "__main__":

    # ================================================================== #
    #                      USER-DEFINED PARAMETERS                       #
    #              >>>>> TO BE EDITED BY THE OPERATOR <<<<<              #
    # ================================================================== #
    
    # Define working directory
    working_dir = Path(r"...")

    # Analysis
    comp_folder = "comparison"

    # Output paths
    fig_file = "overall_comparisons.png"

    # Paths file
    paths_file = Path(r"...") / ".paths.json"

    # Analysis file
    analysis_file = Path(r"...") / "analysis.json"

    # ================================================================== #

    # Go to working directory
    os.chdir(working_dir)

    # Create dictionary containing input data
    dict_inputs = {
        "comp_folder": comp_folder,
    }
    
    # Create process
    process = TrajectoryAnalysisProc(
        dict_inputs=dict_inputs,
        set_inputs=True,
    )
    process.is_case = False

    # Define output paths
    process.output_paths["fig_file"] = fig_file

    # Get dictionary of paths
    with open(paths_file) as f:
        process.dict_paths = json.load(f)

    # Get dictionary of analysis settings
    with open(analysis_file) as f:
        process.dict_analysis = json.load(f) 

    # Run process
    process()
    process.finalize()