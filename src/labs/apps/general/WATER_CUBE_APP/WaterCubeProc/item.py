import os
import attrs
import numpy as np
# import pandas as pd
# import glfw
# from OpenGL.GL import glGetString, GL_VERSION
import genesis as gs
from pathlib import Path

from nuremics import Process

def write_vtk_points(filename, points):
    N = points.shape[0]
    with open(filename, 'w') as f:
        f.write('# vtk DataFile Version 3.0\n')
        f.write('Particle data\n')
        f.write('ASCII\n')
        f.write('DATASET POLYDATA\n')
        f.write(f'POINTS {N} float\n')
        for p in points:
            f.write(f'{p[0]} {p[1]} {p[2]}\n')

@attrs.define
class WaterCubeProc(Process):

    # # Parameters
    # radius: float = attrs.field(init=False, metadata={"input": True})
    # n_sides: int = attrs.field(init=False, metadata={"input": True})
  
    # # Paths
    # title_file: Path = attrs.field(init=False, metadata={"input": True}, converter=Path)

    # # Internal
    # df_points: pd.DataFrame = attrs.field(init=False)

    def __call__(self):
        super().__call__()

        self.water_cube()

    def water_cube(self):

        ########################## init ##########################
        gs.init(backend=gs.cpu)

        ########################## create a scene ##########################
        scene = gs.Scene(
            sim_options=gs.options.SimOptions(
                dt=4e-3,
                substeps=10,
            ),
            sph_options=gs.options.SPHOptions(
                lower_bound=(-0.5, -0.5, 0.0),
                upper_bound=(0.5, 0.5, 1),
                particle_size=0.01,
            ),
            vis_options=gs.options.VisOptions(
                visualize_sph_boundary=True,
            ),
            show_viewer=False,
        )

        ########################## entities ##########################
        plane = scene.add_entity(
            morph=gs.morphs.Plane(),
        )

        liquid = scene.add_entity(
            material=gs.materials.SPH.Liquid(
                sampler='pbs',
            ),
            morph=gs.morphs.Box(
                pos=(0.0, 0.0, 0.65),
                size=(0.4, 0.4, 0.4),
            ),
            surface=gs.surfaces.Default(
                color=(0.4, 0.8, 1.0),
                vis_mode='particle',
            ),
        )

        ########################## build ##########################
        scene.build()

        horizon = 10
        for i in range(horizon):
            scene.step()
            
            particles = liquid.get_particles()  # récupère particules à l’itération i
            np.savetxt(f"frame_{i:06d}.csv", particles, delimiter=',', header='x,y,z', comments='')

            # Sauvegarde au format VTK pour Paraview
            write_vtk_points(f"frame_{i:06d}.vtk", particles)
    
            # # sauvegarde au format .ptc (ou autre format supporté)
            # gs.io.write_ptc(f"frame_{i:06d}.ptc", particles)

        # # get particle positions
        # particles = liquid.get_particles()

        # print(particles)


if __name__ == "__main__":
    
    # ================================================================== #
    #                      USER-DEFINED PARAMETERS                       #
    #              >>>>> TO BE EDITED BY THE OPERATOR <<<<<              #
    # ================================================================== #

    # Working directory
    working_dir = Path(r"...")
    
    # Input parameters
    radius = 0.5
    n_sides = 3
    
    # Input paths
    title_file = Path(r"...") / "plot_title.txt"

    # Output paths
    coords_file = "points_coordinates.csv"
    fig_file = "polygon_shape.png"

    # ================================================================== #

    # Go to working directory
    os.chdir(working_dir)

    # Create dictionary containing input data
    dict_inputs = {
        "radius": radius,
        "n_sides": n_sides,
        "title_file": title_file,
    }
    
    # Create process
    process = PolygonGeometryProc(
        dict_inputs=dict_inputs,
        set_inputs=True,
    )

    # Define output paths
    process.output_paths["coords_file"] = coords_file
    process.output_paths["fig_file"] = fig_file

    # Run process
    process()
    process.finalize()