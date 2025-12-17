import json
import subprocess
from pathlib import Path


def label_entities(
    dim: int,
    infile: Path,
    outfile: str,
):
    """
    Label geometric entities on a CAD model and export the labeling information.

    Depending on the specified dimension, this function identifies
    key entities (constraints, loads, domain) on the geometry and
    stores their indices in a JSON file. It also launches an interactive
    viewer for the user to visualize and verify the labeled entities.

    Parameters
    ----------
    dim : int
        Dimension of the geometry model:
        - 1 for a 1D line (beam)
        - 2 for a 2D surface (plate)
        - 3 for a 3D volume (block)
    infile : Path
        Path to the input CAD file (without extension). The function
        automatically appends ".step" for 2D/3D models or ".brep" for 1D models.
    outfile : str
        Path to the output JSON file where the labeling information
        (entity indices for constraints, loads, and domain) will be saved.
    """

    # ------------------------------------------------------------------- #
    # Assign default entity indices and filename based on model dimension #
    # ------------------------------------------------------------------- #
    if dim == 3:
        # 3D model (volume)
        ids_constraint = [1]
        ids_load = [2]
        filename = str(infile)+".step"
    
    elif dim == 2:
        # 2D model (surface)
        ids_constraint = [4]
        ids_load = [2]
        filename = str(infile)+".step"
    
    elif dim == 1:
        # 1D model (line/beam)
        ids_constraint = [1]
        ids_load = [2]
        filename = str(infile)+".brep"

    # ---------------------------------------------- #
    # Create a dictionary storing entity information #
    # ---------------------------------------------- #
    dict_labels = {
        "Constraint": {
            "dim": dim-1,
            "ids": ids_constraint,
        },
        "Load": {
            "dim": dim-1,
            "ids": ids_load,
        },
        "Domain": {
            "dim": dim,
            "ids": [1],
        },
    }

    # ---------------------------------------------- #
    # Export the labeling information to a JSON file #
    # ---------------------------------------------- #
    with open(outfile, "w") as f:
        json.dump(dict_labels, f, indent=4)

    # ------------------------------------------------------------------ #
    # Launch interactive visualization for each label (excluding Domain) #
    # ------------------------------------------------------------------ #
    for key, value in dict_labels.items():
        if key != "Domain":
            ids_str = ",".join(str(i) for i in value["ids"])
            subprocess.run([
                "python", "-m", "labs.ops.cms.labeling.visualize_label",
                filename,           # CAD file to display
                key,                # Label name (Constraint or Load)
                str(value["dim"]),  # Dimension of sub-entities to visualize
                ids_str,            # List of entity IDs to highlight
            ])