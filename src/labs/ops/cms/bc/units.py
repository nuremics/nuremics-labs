from pathlib import Path
from PyQt6.QtWidgets import QApplication
from OCC.Display.backend import load_backend
load_backend("pyqt6")
from OCC.Display.qtDisplay import qtViewer3d
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.BRepTools import breptools
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.BRep import BRep_Builder
from OCC.Core.Graphic3d import Graphic3d_NameOfMaterial
from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_FACE, TopAbs_EDGE, TopAbs_VERTEX
from OCC.Core.Graphic3d import Graphic3d_NameOfMaterial


def visualize_boundary_condition(
    filename: str,
    label: str,
    entity: str,
    ids: list,
):
    """
    Display a CAD geometry in an interactive PyQt6 window using pythonOCC-core.

    The function loads a CAD geometry (e.g., STEP or BREP), initializes
    a PyQt6 application, creates a 3D viewer, and displays the geometry.
    The viewer supports rotation, zoom, and pan. The display session is
    automatically created and closed within the function, so the user can
    interact with the geometry without affecting the rest of the Python program.

    Parameters
    ----------
    filename : str
        Path to the input CAD file (STEP, BREP, or other supported formats)
        that will be opened and displayed in Gmsh.
    """
    
    file_path = Path(filename)
    ext = file_path.suffix.lower() 
    
    if ext == ".step":
        reader = STEPControl_Reader()
        reader.ReadFile(filename)
        reader.TransferRoot()
        shape = reader.Shape()
    
    elif ext == ".brep":
        shape = TopoDS_Shape()
        builder = BRep_Builder()
        breptools.Read(shape, filename, builder)

    # Create Qt application
    app = QApplication([])
    viewer = qtViewer3d()
    viewer.create()
    viewer.InitDriver()

    # Display shape
    viewer._display.DisplayShape(
        shapes=shape,
        material=Graphic3d_NameOfMaterial.Graphic3d_NOM_METALIZED,
        color="ORANGE",
        transparency=0.7,
    )

    # Explore entities
    if entity == "face":
        exp = TopExp_Explorer(shape, TopAbs_FACE)
    elif entity == "edge":
        exp = TopExp_Explorer(shape, TopAbs_EDGE)
    elif entity == "vertex":
        exp = TopExp_Explorer(shape, TopAbs_VERTEX)

    index = 1
    while exp.More():
        face = exp.Current()
        if index in ids:
            viewer._display.DisplayShape(
                shapes=face,
                material=Graphic3d_NameOfMaterial.Graphic3d_NOM_METALIZED,
                color="RED",
                transparency=0.0,
            )
        exp.Next()
        index += 1

    viewer.setWindowTitle(f"Boundary Condition: {label}")
    # viewer.setWindowIcon(QIcon(r"C:\Users\julie\GitRepo\nuremics-docs\docs\images\logo.png"))
    viewer._display.FitAll()
    viewer.show()
    app.exec()
    viewer.close()