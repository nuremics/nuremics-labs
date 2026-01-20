from pathlib import Path
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.BRepTools import breptools
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.BRep import BRep_Builder
from OCC.Core.Graphic3d import Graphic3d_NameOfMaterial
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_SOLID, TopAbs_FACE, TopAbs_EDGE, TopAbs_VERTEX
from OCC.Core.Graphic3d import Graphic3d_NameOfMaterial
from OCC.Core.Quantity import Quantity_Color, Quantity_TOC_RGB
from OCC.Display.SimpleGui import init_display
from PyQt6.QtWidgets import QApplication
# from importlib.resources import files


def visualize_label(
    filename: str,
    label: str,
    dim: int,
    ids: list,
):
    """
    Visualize labeled geometric entities on a CAD model.

    This function loads a CAD geometry from a STEP or BREP file and opens
    an interactive PyQt6 / pythonOCC viewer. The full geometry is displayed
    semi-transparently, while a selected subset of entities
    (faces, edges, or vertices) corresponding to a given label
    is highlighted for visual inspection.

    Parameters
    ----------
    filename : str
        Path to the CAD file to be displayed. Supported formats are
        `.step` for 2D and 3D models and `.brep` for 1D models.
    label : str
        Name of the label associated with the geometric entities being
        visualized. This value is displayed in the viewer window title.
    dim : int
        Topological dimension of the entities to highlight:
        - 3 → solids
        - 2 → faces
        - 1 → edges
        - 0 → vertices
    ids : list of int
        List of indices of the geometric entities to be highlighted.
        Indices start from 1 and follow the exploration order defined
        by OpenCascade.
    """
    
    # ----------------- #
    # Load CAD geometry #
    # ----------------- #
    file_path = Path(filename)
    ext = file_path.suffix.lower() 
    
    if ext == ".step":
        # Read STEP geometry (2D or 3D models)
        reader = STEPControl_Reader()
        reader.ReadFile(filename)
        reader.TransferRoot()
        shape = reader.Shape()
    
    elif ext == ".brep":
        # Read BREP geometry (1D models)
        shape = TopoDS_Shape()
        builder = BRep_Builder()
        breptools.Read(shape, filename, builder)

    # ------------------ #
    # Initialize display #
    # ------------------ #
    display, start_display, add_menu, add_function_to_menu = \
        init_display(
            display_triedron=False,
            background_gradient_color1=[30, 30, 30],
            background_gradient_color2=[30, 30, 30],
        )

    # ---------------------------------------- #
    # Display full geometry (semi-transparent) #
    # ---------------------------------------- #
    display.DisplayShape(
        shapes=shape,
        material=Graphic3d_NameOfMaterial.Graphic3d_NOM_METALIZED,
        color="orange",
        transparency=0.7,
    )

    # --------------------------------------------- #
    # Select entities to explore based on dimension #
    # --------------------------------------------- #
    if dim == 3:
        # Explore solids
        exp = TopExp_Explorer(shape, TopAbs_SOLID)
    elif dim == 2:
        # Explore faces
        exp = TopExp_Explorer(shape, TopAbs_FACE)
    elif dim == 1:
        # Explore edges
        exp = TopExp_Explorer(shape, TopAbs_EDGE)
    elif dim == 0:
        # Explore vertices
        exp = TopExp_Explorer(shape, TopAbs_VERTEX)

    # --------------------------- #
    # Highlight selected entities #
    # --------------------------- #
    index = 1  # OpenCascade exploration indices start at 1
    light_blue = Quantity_Color(0.0, 0.78, 0.75, Quantity_TOC_RGB)

    while exp.More():
        entity = exp.Current()
        if index in ids:
            # Highlight entities corresponding to the given label
            display.DisplayShape(
                shapes=entity,
                material=Graphic3d_NameOfMaterial.Graphic3d_NOM_METALIZED,
                color=light_blue,
                transparency=0.0,
            )
        exp.Next()
        index += 1

    display.FitAll()

    app = QApplication.instance()
    windows = app.topLevelWidgets()
    windows[0].setWindowTitle(f"Label: {label}")

    start_display()