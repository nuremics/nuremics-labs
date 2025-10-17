import os
import attrs
import json
from pathlib import Path

from nuremics import Process
from labs.apps.cms.CANTILEVER_SHEAR_APP.procs.MeshProc.ops import (
    create_mesh,
)


@attrs.define
class MeshProc(Process):
    """
    Create a geometric representation of a physical system.

    Process
    -------
        A/ create_geometry
            Create and export a simple geometric entity (beam, plate, or block)
            in STEP or BREP format.

    Input parameters
    ----------------
        dim : int
            Dimension of the geometry: 
            1 for a line (beam), 2 for a rectangle (plate), 3 for a box (block).
        length : float
            Length of the geometry along the X axis.
        width : float
            Width of the geometry along the Y axis (only used if dim = 2/3).
        height : float
            Height of the geometry along the Z axis (only used if dim = 3).

    Outputs (stored in self.output_paths)
    -------
        outfile : .step or .brep
            File containing the created geometry (in .step if dim = 3/2 or .brep if dim = 1).
    """

    # Parameters
    dim: int = attrs.field(init=False, metadata={"input": True})

    # Paths
    mesh_settings_file: Path = attrs.field(init=False, metadata={"input": True}, converter=Path)
    infile: Path = attrs.field(init=False, metadata={"input": True}, converter=Path)

    def __call__(self):
        super().__call__()

        self.create_mesh()

    def create_mesh(self):
        """
        Create and export a simple geometric entity (beam, plate, or block)
        in STEP or BREP format.

        Uses
        ----
            dim
            length
            width
            height
        
        Generates
        ---------
            outfile
        """

        # Load mesh settings
        with open(self.mesh_settings_file) as f:
            dict_mesh_settings = json.load(f)

        # create_mesh(
        #     infile=self.infile,
        #     outfile=self.output_paths["outfile"],
        #     dim=self.dim,
        #     elem=dict_mesh_settings["elem"],
        #     dx=dict_mesh_settings["dx"],
        #     nb_elem_length=dict_mesh_settings["nb_elem_length"],
        #     nb_elem_width=dict_mesh_settings["nb_elem_width"],
        #     nb_elem_height=dict_mesh_settings["nb_elem_height"],
        #     silent=self.silent,
        # )


if __name__ == "__main__":

    # ================================================================== #
    #                      USER-DEFINED PARAMETERS                       #
    #              >>>>> TO BE EDITED BY THE OPERATOR <<<<<              #
    # ================================================================== #

    # Working directory
    working_dir = Path(r"...")

    # Input parameters
    dim = 3
    length = 10.0 
    width = 1.0
    height = 0.1

    # Output paths
    outfile = "geometry"

    # ================================================================== #

    # Go to working directory
    os.chdir(working_dir)

    # Create dictionary containing input data
    dict_inputs = {
        "dim": dim,
        "length": length,
        "width": width,
        "height": height,
    }

    # Create process
    process = GeometryProc(
        dict_inputs=dict_inputs,
        set_inputs=True,
    )

    # Define output paths
    process.output_paths["outfile"] = outfile

    # Run process
    process()
    process.finalize()