"""
Subprocess entry point for executing the function `visualize_geometry_occ`.

This module is intended to be executed as a standalone Python script
(e.g., via `python -m`) from another process. It acts as a thin wrapper
that parses command-line arguments and invokes the function in a
separate isolated Python process using `subprocess`.

This pattern ensures that the execution context of the called function
is fully isolated from the caller.
"""

import sys
from .units import visualize_geometry_occ


# ------------------------------- #
# Retrieve command-line arguments #
# ------------------------------- #
filename = sys.argv[1]

# ---------------------------------------------------- #
# Call the function in the isolated subprocess context #
# ---------------------------------------------------- #
visualize_geometry_occ(
    filename=filename,
)