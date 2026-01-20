import os
import re
import json
import subprocess
from pathlib import Path

from labs.ops.cms.geometry import visualize_geometry_gmsh
from labs.ops.cms.labeling import visualize_label


def label_entities(
    dim: int,
    automatic: bool,
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
    automatic : bool
        If `True`, labeling is done automatically.
        If `False`, labeling is done manually using the Gmsh GUI.
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
    if (dim == 3) or (dim == 2):
        # 3D model (volume) / 2D model (surface)
        filename = str(infile)+".step"
    
    elif dim == 1:
        # 1D model (line/beam)
        filename = str(infile)+".brep"

    # ---------------------------------------------- #
    # Create a dictionary storing entity information #
    # ---------------------------------------------- #
    if automatic:
        # List of ids corresponding to each label is 
        # retrieved from the CAD automatic generation
        if dim == 3:
            # 3D model (volume)
            ids_constraint = [1]
            ids_load = [2]
        
        elif dim == 2:
            # 2D model (surface)
            ids_constraint = [4]
            ids_load = [2]
        
        elif dim == 1:
            # 1D model (line/beam)
            ids_constraint = [1]
            ids_load = [2]
        
        # Define dictionary containing the labeled entities
        dict_labels = {
            "Constraint": {
                "dim": dim-1,
                "ids": ids_constraint,
            },
            "Load": {
                "dim": dim-1,
                "ids": ids_load,
            },
            "Body": {
                "dim": dim,
                "ids": [1],
            },
        }
    
    else:
        # Labels must be defined by the operator from the Gmsh GUI
        if not os.path.isfile(str(infile)+".geo"):
            visualize_geometry_gmsh(
                filename=filename,
            )

        # Initialize dictionary containing the labeled entities
        dict_labels = {}

        # Dictionary to map the type to dimension
        dim_map = {
            "Point": 0,
            "Curve": 1,
            "Surface": 2,
            "Volume": 3
        }

        # Regular expression to extract the information
        pattern = re.compile(r'Physical\s+(Point|Curve|Surface|Volume)\s*\("([^"]+)"\s*,\s*\d+\)\s*=\s*{([^}]+)}')

        with open(str(infile)+".geo", "r") as f:
            for line in f:
                line = line.strip()
                # Check if the line contains "Physical"
                if "Physical" in line:
                    match = pattern.search(line)
                    if match:
                        phys_type = match.group(1)  # Extract type (Point, Curve, Surface, Volume)
                        label = match.group(2)      # Extract label name
                        ids_str = match.group(3)    # Extract IDs inside {}

                        # Convert IDs to a list of integers
                        ids = [int(x.strip()) for x in ids_str.split(",") if x.strip().isdigit()]

                        # Add to the dictionary
                        dict_labels[label] = {
                            "dim": dim_map[phys_type],
                            "ids": ids
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
        # if key != "Domain":
        ids_str = ",".join(str(i) for i in value["ids"])
        subprocess.run([
            "python", "-m", "labs.ops.cms.labeling.visualize_label",
            filename,           # CAD file to display
            key,                # Label name (Constraint or Load)
            str(value["dim"]),  # Dimension of sub-entities to visualize
            ids_str,            # List of entity IDs to highlight
        ])