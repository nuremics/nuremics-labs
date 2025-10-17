from pathlib import Path

from labs.ops.cms.bc import visualize_boundary_condition


def set_boundary_conditions(
    infile: Path,
    dim: int,
):
    
    if dim == 3:
        entity = "face"
        ids_constraint = [1]
        ids_load = [2]
        filename = str(infile)+".step"
    
    elif dim == 2:
        entity = "edge"
        ids_constraint = [4]
        ids_load = [2]
        filename = str(infile)+".step"
    
    elif dim == 1:
        entity = "vertex"
        ids_constraint = [1]
        ids_load = [2]
        filename = str(infile)+".brep"

    visualize_boundary_condition(
        filename=filename,
        label="Constraint",
        entity=entity,
        ids=ids_constraint,
    )

    visualize_boundary_condition(
        filename=filename,
        label="Load",
        entity=entity,
        ids=ids_load,
    )