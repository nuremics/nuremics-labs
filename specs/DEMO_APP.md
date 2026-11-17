# [DEMO_APP](../src/nuremics_labs/apps/general/DEMO_APP/)

This document is the Functional Requirements Specification (FRS) of the app `DEMO_APP`. It is the north star of the development: every component of the app derives from it, and it is refined as the implementation progresses. An early draft states the intent; implementing a requirement sharpens it; the document is updated before the code when a requirement changes.

Each functional requirement (FR-1, FR-2, ...) defines one processing step of the app, implemented as one nuRemics process (proc) carrying the same name. Requirements can be written before their proc exists.

## 1. Context

- The app is the demonstration application of the nuRemics framework: it exercises the mechanics every app relies on, a workflow of chained processes sharing parameters and paths, and a closing overall analysis, on a scientific scenario simple enough to be verified by hand.
- The scenario studies the planar flight of a polygonal rigid body launched under gravity: the trajectory recorded by a two-dimensional physics simulation is compared with the analytical solution of projectile motion.
- The body is defined by its cross-section, a regular polygon given by the radius of its circumscribed circle and its number of sides.
- The launch conditions (initial speed and angle) and the physical parameters (gravity, mass) are provided by the operator, together with the simulation configuration (solver timestep, rendering frame rate and window size).
- Several cases (distinct launch conditions or shapes) can be processed by the same workflow; their comparisons are assembled by the closing analysis step.

## 2. Purpose

The app validates the framework chain end to end on a scenario whose reference solution is known analytically: a polygonal rigid body is generated, launched as a projectile in a two-dimensional physics simulation, and its simulated trajectory is compared, time step by time step, with the analytical trajectory derived from the same initial conditions. It turns a set of operator-provided physical inputs into per-case trajectory comparisons and one overall comparative figure, so that the framework's parameter/path wiring, case handling and analysis layer are demonstrated on a complete, self-contained and verifiable example.

## 3. Overview

### Inputs

- **Body shape**: the regular polygon of the body, defined by its circumscribed-circle radius and its number of sides.
- **Launch conditions**: the initial velocity of the projectile, as a magnitude and an angle from horizontal.
- **Physical parameters**: the gravitational acceleration and the mass of the body.
- **Simulation configuration**: the solver timestep and the display configuration (frame rate, window size).
- **Plot title**: the title text of the body shape figure.

### Outputs

- **Body geometry**: the vertex coordinates of the polygon and the plotted figure of the shape.
- **Trajectory comparison**: per case, one spreadsheet holding the simulated and analytical trajectories and one figure comparing both.
- **Overall analysis**: one comparative plot assembling every processed case against the theory.

### Processing

Taken as a whole, the app is a black box that reads the inputs and generates the outputs. The regular polygon of the body is generated from its radius and number of sides and plotted; the body is launched with the provided initial conditions in a two-dimensional physics simulation, whose recorded trajectory is compared with the analytical trajectory computed from the same initial conditions; the comparisons of all cases are finally assembled into one overall comparative plot.

All steps obey the same rules:

- **Analytical reference.** The theoretical trajectory follows the closed-form equations of projectile motion (uniform horizontal motion, uniformly accelerated vertical motion); every comparison inherits the validity of this reference.
- **Read-as-provided inputs.** The operator-provided files (plot title, launch conditions, simulation configuration) are read as-is, never modified.
- **Deterministic and traceable.** Re-running a step with the same inputs reproduces the same artifacts, and the framework records the inputs of every step, so each artifact is traceable to the shape, launch conditions and configuration it derives from.

## 4. Functional requirements

### FR-1: [PolygonGeometryProc](../src/nuremics_labs/procs/general/PolygonGeometryProc/)

#### Description

Generates the regular polygon of the body and plots its shape.

#### Purpose

The simulation launches a rigid body whose cross-section is a regular polygon: the polygon defines the geometry the physics engine instantiates, and its figure documents the shape actually used by the case. Without this step, the body geometry exists only as two abstract parameters, with no artifact to inspect and no coordinates to feed the simulation.

#### Inputs

- The circumscribed-circle radius and the number of sides of the polygon.
- The plot title text.

#### Outputs

- The vertex coordinates of the polygon (CSV file).
- The figure of the plotted polygon (PNG image).

#### Processing

The vertices are computed on the circumscribed circle, counter-clockwise from angle zero, centered at the origin, and written to a CSV file. The closed polygon is then plotted from these vertices, titled with the provided text, and saved as a figure.

### FR-2: [ProjectileModelProc](../src/nuremics_labs/procs/general/ProjectileModelProc/)

#### Description

Simulates the flight of the polygonal body and compares its trajectory with the analytical solution.

#### Purpose

The comparison of the simulated trajectory with the analytical solution is the core of the demonstration: it shows the framework carrying a numerical model and its theoretical reference through the same chain, to a shared comparison artifact. This step produces that comparison for one case, from the body geometry and the physical inputs of the case.

#### Inputs

- The physical parameters: gravitational acceleration and body mass.
- The launch conditions: initial speed and angle.
- The simulation configuration: solver timestep, rendering frame rate and window size.
- The vertex coordinates of the body polygon (FR-1 output).

#### Outputs

- The comparison folder of the case: the spreadsheet holding both trajectories and the figure comparing them.

#### Processing

The polygon vertices are read and the body is created from them, centered on its centroid and launched with the initial velocity in a two-dimensional physics space holding a static ground segment and a vertical wall. The simulation advances by the configured timestep, displaying the flight when not silent, and the body position is recorded at each step until the first contact with the ground. The analytical trajectory is computed at the same time steps from the same initial height, speed and angle. Both trajectories are written to one spreadsheet, and a figure comparing the model trajectory with the theory is saved in the comparison folder.

### FR-3: [TrajectoryAnalysisProc](../src/nuremics_labs/procs/general/TrajectoryAnalysisProc/)

#### Description

Assembles the trajectory comparisons of every processed case into one overall comparative plot.

#### Purpose

Each case produces its own comparison figure, but the demonstration scenario is meant to be run over several configurations (shapes, launch conditions, parameters): the overall analysis gives the single figure where every case is read against the same theoretical reference, which is the deliverable of the demonstration.

#### Inputs

- The comparison folder of each case, holding its spreadsheet of simulated and analytical trajectories (FR-2 output).

#### Outputs

- The overall comparative plot of all cases against the theory (PNG image).

#### Processing

The step is a framework analysis: it reads each case spreadsheet, plots the theoretical trajectory once, and plots the simulated trajectory of each case included by the analysis settings, styled by those settings (color, line style, marker, legend label). The overall figure is saved as the closing artifact of the app.

## 5. Open points

- The demonstration scenario is intentionally complete and minimal: no requirement beyond the three steps is foreseen; new demonstration capabilities would be added as new functional requirements when identified.
- The physics of the simulation step (contact handling, recording until first ground contact) is fixed by the demonstration purpose; a more faithful projectile model (air drag, rebound) is out of scope and would be a new requirement if ever needed.
