import gmsh
from pathlib import Path


def create_mesh(
    infile: Path,
    outfile: str,
    dim: int,
    elem: str,
    dx: float = None,
    nb_elem_length: int = None,
    nb_elem_width: int = None,
    nb_elem_height: int = None,
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

    # Initialize gmsh
    gmsh.initialize()
    gmsh.clear()

    # Open geometry file
    if (dim == 3) or (dim == 2):
        geometry_path = str(infile)+".step"
    else:
        geometry_path = str(infile)+".brep"
    gmsh.open(geometry_path)

    # Synchronize gmsh
    gmsh.model.occ.synchronize()

    # Get geometry dimensions
    volumes = gmsh.model.occ.getEntities(dim=3)
    dim, tag = volumes[0]
    xmin, ymin, zmin, xmax, ymax, zmax = gmsh.model.occ.getBoundingBox(dim, tag)
    length = xmax - xmin
    width = ymax - ymin
    height = zmax - zmin

    # Add physical groups
    gmsh.model.addPhysicalGroup(
        dim=dim,
        tags=[1],
        tag=1,
        name="domain",
    )
    gmsh.model.addPhysicalGroup(
        dim=dim-1,
        tags=[1],
        tag=2,
        name="constraint",
    )
    gmsh.model.addPhysicalGroup(
        dim=dim-1,
        tags=[2],
        tag=3,
        name="load",
    )

    # num_nodes_length = 2
    # num_nodes_width = 2
    # if dx is not None:
    #     num_nodes_length = int(0.5+length/dx)+1
    #     num_nodes_width = int(0.5+width/dx)+1
    # if nb_elem_length is not None:
    #     num_nodes_length = nb_elem_length+1
    # if nb_elem_width is not None:
    #     num_nodes_width = nb_elem_width+1

    # if dim == 3:
    #     num_nodes_height = 2
    #     if dx is not None:
    #         num_nodes_height = int(0.5+height/dx)+1
    #     if nb_elem_height is not None:
    #         num_nodes_height = nb_elem_height+1

    # if dim == 3:

    #     if (elem == "hexa") or (elem == "tetra"):

    #         for tag in [9, 10, 11, 12]:
    #             gmsh.model.mesh.setTransfiniteCurve(
    #                 tag=tag,
    #                 numNodes=num_nodes_length,
    #             )
    #         for tag in [2, 4, 6, 8]:
    #             gmsh.model.mesh.setTransfiniteCurve(
    #                 tag=tag,
    #                 numNodes=num_nodes_width,
    #             )
    #         for tag in [1, 3, 5, 7]:
    #             gmsh.model.mesh.setTransfiniteCurve(
    #                 tag=tag,
    #                 numNodes=num_nodes_height,
    #             )
    #         for tag in [1, 2, 3, 4, 5, 6]:
    #             gmsh.model.mesh.setTransfiniteSurface(
    #                 tag=tag,
    #             )
    #             if (elem == "hexa"):
    #                 gmsh.model.mesh.setRecombine(
    #                     dim=2,
    #                     tag=tag,
    #                 )
    #         gmsh.model.mesh.setTransfiniteVolume(
    #             tag=1,
    #         )
    #         if (elem == "hexa"):
    #             gmsh.model.mesh.recombine()
        
    #     elif elem == "utetra":

    #         gmsh.option.setNumber("Mesh.MeshSizeMax", dx)
    
    # # else:

    # #     if (elem == "quad"):

    # #         for tag in [1, 3]:
    # #             gmsh.model.mesh.setTransfiniteCurve(
    # #                 tag=tag,
    # #                 numNodes=num_nodes_length,
    # #             )
    # #         for tag in [2, 4]:
    # #             gmsh.model.mesh.setTransfiniteCurve(
    # #                 tag=tag,
    # #                 numNodes=num_nodes_width,
    # #             )
    # #         gmsh.model.mesh.setTransfiniteSurface(
    # #                 tag=1,
    # #             )
    # #         gmsh.model.mesh.setRecombine(
    # #             dim=dim,
    # #             tag=1,
    # #         )

    # #     elif (elem == "tri"):
    # #         gmsh.option.setNumber("Mesh.MeshSizeMax", dx)
    
    # # Generate mesh
    # gmsh.model.mesh.generate(dim)

    # # Show surface faces of the mesh
    # gmsh.option.setNumber("Mesh.SurfaceFaces", 1)
    
    # # Launch gmsh
    # if not silent:
    #     gmsh.fltk.run()

    # # Save mesh file
    # gmsh.option.setNumber("Mesh.MshFileVersion", 4.1)
    # gmsh.write(outfile)

    gmsh.write("my_model.geo_unrolled")
    
    # Finalize gmsh
    gmsh.clear()
    gmsh.finalize()