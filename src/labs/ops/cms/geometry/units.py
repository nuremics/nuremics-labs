import gmsh

def visualize_geometry(
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