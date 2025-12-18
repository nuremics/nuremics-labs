"""
Subprocess entry point for executing the function `visualize_label`.

This module is intended to be executed as a standalone Python script
(e.g., via `python -m`) from another process. It acts as a thin wrapper
that parses command-line arguments and invokes the function in a
separate isolated Python process using `subprocess`.

This pattern ensures that the execution context of the called function
is fully isolated from the caller.
"""

import sys
from .units import visualize_label


# ------------------------------- #
# Retrieve command-line arguments #
# ------------------------------- #
filename = sys.argv[1]
label = sys.argv[2]
dim = int(sys.argv[3])
ids = [int(x) for x in sys.argv[4].split(",")]

# ---------------------------------------------------- #
# Call the function in the isolated subprocess context #
# ---------------------------------------------------- #
visualize_label(
    filename=filename,
    label=label,
    dim=dim,
    ids=ids,
)