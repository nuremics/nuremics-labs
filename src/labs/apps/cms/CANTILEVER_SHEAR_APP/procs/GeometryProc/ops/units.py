import sys
import cadquery as cq
from cadquery import exporters

from labs.ops.cms.geometry import visualize_geometry_gmsh


def create_geometry(
    dim: int,
    length: float,
    width: float,
    height: float,
    outfile: str,
    silent: bool = False,
):
    """
    Create and export a simple geometric entity (beam, plate, or block)
    in STEP or BREP format.

    Depending on the specified dimension, this function generates:
    - A 3D rectangular block (box) exported as STEP.
    - A 2D rectangular surface (plate) exported as STEP.
    - A 1D line (beam) exported as BREP.

    Parameters
    ----------
    dim : int
        Dimension of the geometry: 
        1 for a line (beam), 2 for a rectangle (plate), 3 for a box (block).
    length : float
        Length of the geometry along the X axis.
    width : float
        Width of the geometry along the Y axis (only used if dim = 2/3).
    height : float
        Height of the geometry along the Z axis (only used if dim = 3).
    outfile : str
        Base name of the output file where the created geometry 
        will be saved. The function automatically appends the appropriate 
        extension (.step or .brep).
    silent : bool (default is False)
        If False, the geometry will be displayed interactively.
    """

    # 3D plate
    if dim == 3:
        geometry = cq.Workplane("front").box(
            length=length,
            width=width,
            height=height,
            centered=[False, True, True],
        )
        ext = ".step"
    
    # 2D shell
    elif dim == 2:
        wire = cq.Workplane("XY").rect(
            xLen=length,
            yLen=width,
            centered=[False, True]
        ).toPending().consolidateWires().val()
        geometry = cq.Face.makeFromWires(wire)
        ext = ".step"

    # 1D beam
    elif dim == 1:
        geometry = cq.Workplane("XY").moveTo(0, 0).lineTo(length, 0)
        ext = ".brep"
    
    else:
        sys.exit("Dimension must be either 1, 2 or 3.")

    # Export geometry
    exporters.export(geometry, outfile+ext)

    # View geometry
    if not silent:
        visualize_geometry_gmsh(
            filename=outfile+ext,
        )