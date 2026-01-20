import os
import attrs
from pathlib import Path

from nuremics import Process
from labs.apps.cms.CANTILEVER_SHEAR_APP.procs.LabelingProc.ops import (
    label_entities,
)


@attrs.define
class LabelingProc(Process):
    """
    Define and label the entities of a physical system from its geometric representation.

    Process
    -------
        A/ label_entities
            Assign labels to the entities of a geometric model.

    Input parameters
    ----------------
        dim : int
            Dimension of the geometry: 
            1 for a line (beam), 2 for a rectangle (plate), 3 for a box (block).
        automatic : bool
            If `True`, labeling is done automatically.
            If `False`, labeling is done manually using the Gmsh GUI.

    Input paths
    -----------
        infile : .step or .brep
            File containing the geometric model (in .step if dim = 3|2 or .brep if dim = 1).

    Outputs (stored in self.output_paths)
    -------
        outfile : .json
            File containing the labeled geometric entities.
    """

    # Parameters
    dim: int = attrs.field(init=False, metadata={"input": True})
    automatic: bool = attrs.field(init=False, metadata={"input": True})

    # Paths
    infile: Path = attrs.field(init=False, metadata={"input": True}, converter=Path)

    def __call__(self):
        super().__call__()

        self.label_entities()

    def label_entities(self):
        """
        Assign labels to the entities of a geometric model.

        Uses
        ----
            dim
            automatic
            infile
        
        Generates
        ---------
            outfile
        """
        
        label_entities(
            dim=self.dim,
            automatic=self.automatic,
            infile=self.infile,
            outfile=self.output_paths["outfile"],
        )


if __name__ == "__main__":

    # ================================================================== #
    #                      USER-DEFINED PARAMETERS                       #
    #              >>>>> TO BE EDITED BY THE OPERATOR <<<<<              #
    # ================================================================== #

    # Working directory
    working_dir = Path(r"...")

    # Input parameters
    dim = 3

    # Input parameters
    infile = Path(r"...")

    # Output paths
    outfile = "labels.json"

    # ================================================================== #

    # Go to working directory
    os.chdir(working_dir)

    # Create dictionary containing input data
    dict_inputs = {
        "dim": dim,
        "infile": infile,
    }

    # Create process
    process = LabelingProc(
        dict_inputs=dict_inputs,
        set_inputs=True,
    )

    # Define output paths
    process.output_paths["outfile"] = outfile

    # Run process
    process()
    process.finalize()