import gmsh
from pathlib import Path
from OCC.Core.STEPControl import STEPControl_Reader
from OCC.Core.BRepTools import breptools
from OCC.Core.TopoDS import TopoDS_Shape
from OCC.Core.BRep import BRep_Builder
from OCC.Core.Graphic3d import Graphic3d_NameOfMaterial
from OCC.Display.SimpleGui import init_display
from PyQt6.QtWidgets import QApplication


def visualize_geometry_gmsh(
    filename: str,
):
    """
    Display a geometry file in Gmsh.

    The function loads a CAD geometry (e.g., STEP or BREP), 
    synchronizes the model, switches to solid surface visualization, 
    and opens the interactive Gmsh GUI. The session is automatically 
    initialized and finalized within the function.

    Parameters
    ----------
    filename : str
        Path to the input CAD file (STEP, BREP, or other supported formats)
        that will be opened and displayed in Gmsh.
    """
    
    # Initialize gmsh
    gmsh.initialize()
    gmsh.clear()

    # Open input file
    gmsh.open(filename)

    # Synchronize gmh
    gmsh.model.occ.synchronize()

    # Change surface aspect to solid
    gmsh.option.setNumber("Geometry.SurfaceType", 2)
    
    # Launch gmsh
    gmsh.fltk.run()
    
    # Finalize gmsh
    gmsh.clear()
    gmsh.finalize()


def visualize_geometry_occ(
    filename: str,
):
    """
    Display a CAD geometry in an interactive PyQt6 window using pythonOCC-core.

    The function loads a CAD geometry (e.g., STEP or BREP), creates a 3D viewer, 
    and displays the geometry. The viewer supports rotation, zoom, and pan.
    The display session is automatically created and closed within the function,
    so the user can interact with the geometry without affecting the rest of 
    the Python program.

    Parameters
    ----------
    filename : str
        Path to the input CAD file (STEP, BREP, or other supported formats)
        that will be opened and displayed in the 3D viewer.
    """
    
    # --------------- #
    # Import geometry #
    # --------------- #
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
    
    # ------- #
    # Display #
    # ------- #
    display, start_display, add_menu, add_function_to_menu = \
        init_display(
            display_triedron=False,
            background_gradient_color1=[30, 30, 30],
            background_gradient_color2=[30, 30, 30],
        )
    display.DisplayShape(
        shapes=shape,
        material=Graphic3d_NameOfMaterial.Graphic3d_NOM_METALIZED,
        color="orange",
        transparency=0.0,
        update=True,
    )
    display.FitAll()

    app = QApplication.instance()
    windows = app.topLevelWidgets()
    windows[0].setWindowTitle("Geometry")

    start_display()