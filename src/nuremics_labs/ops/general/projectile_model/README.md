# projectile_model — ops

## Functions

- `simulate_projectile_motion`
- `calculate_analytical_trajectory`
- `compare_model_vs_analytical_trajectories`

---

## `simulate_projectile_motion`

### Overview

Simulate the planar flight of a polygonal rigid body launched under gravity.

### Description

Runs the simulation with the pymunk physics engine in a dedicated spawned process, rendered with pygame when `silent` is `False` (square window of `window_size` pixels, scaled to the theoretical flight extent, frame rate capped by `timestep`). The environment holds a static horizontal ground segment and a vertical wall forming a corner beyond the theoretical flight distance. The body is created from the polygon vertices (centered on their centroid), assigned the given `mass` and friction, positioned at an initial height equal to the mean vertex distance, and launched with the velocity components derived from `v0` and `angle`. The position of the body is recorded at each `timestep` from `t=0` until the first contact with the ground occurs; the simulation stops after the theoretical flight time plus two seconds. Raises nothing in normal operation; the recorded trajectory is returned through the process queue.

### Inputs

- **`df_points`** (`pd.DataFrame`) : Vertex coordinates of the body polygon, columns `X` and `Y` (local frame).
- **`mass`** (`float`) : Mass of the body (kg).
- **`gravity`** (`float`) : Gravitational acceleration (m/s²).
- **`v0`** (`float`) : Initial velocity magnitude (m/s).
- **`angle`** (`float`) : Launch angle in degrees, from horizontal.
- **`timestep`** (`float`) : Time increment of the physics simulation steps (s).
- **`fps`** (`int`) : Frame rate of the visual simulation when not silent (default 60).
- **`window_size`** (`int`) : Size in pixels of the square pygame window (default 600).
- **`silent`** (`bool`) : `False` (default) displays the simulation; `True` runs without rendering.

### Outputs

- **`df_trajectory`** (`pd.DataFrame`) : Recorded trajectory of the body, columns `t`, `x_model`, `y_model`, from `t=0` until the first ground contact.

---

## `calculate_analytical_trajectory`

### Overview

Compute the analytical projectile trajectory at the time steps of the model.

### Description

For each time `t` of the input DataFrame, computes the theoretical position of the projectile from the closed-form equations of motion: `x(t) = v0 * cos(angle) * t` (uniform horizontal motion) and `y(t) = h0 + v0 * sin(angle) * t + 0.5 * gravity * t²` (uniformly accelerated vertical motion), where `h0` is the initial height taken from the first recorded model position. The two columns `x_theory` and `y_theory` are appended to the DataFrame and its index is set to `t`. When `filename` is provided, the result is saved to that Excel file (`xlsxwriter` engine, index kept). The input DataFrame is modified in place and returned.

### Inputs

- **`df`** (`pd.DataFrame`) : Simulated trajectory holding the time column `t` (s), from `simulate_projectile_motion`.
- **`v0`** (`float`) : Initial velocity magnitude (m/s).
- **`angle`** (`float`) : Launch angle in degrees, from horizontal.
- **`gravity`** (`float`) : Gravitational acceleration (m/s²).
- **`filename`** (`Optional[Path]`) : Excel file to write both trajectories to; skipped when `None`.

### Outputs

- **`df`** (`pd.DataFrame`) : The input DataFrame extended with `x_theory` and `y_theory` (m), indexed by `t`.

---

## `compare_model_vs_analytical_trajectories`

### Overview

Plot the simulated trajectory against the analytical one and save the comparison.

### Description

Plots the theoretical trajectory as a solid black line (legend `Theory`) and the simulated trajectory as a dashed red line (legend `Model`) in the same axes. The title `(x, y) trajectory: model vs. theory`, the axis labels (`x (m)`, `y (m)`), an equal aspect ratio, a legend and a grid are applied, the nuRemics logo is inserted in the plot background, and the figure is saved to `filename` at 300 dpi. When `silent` is `False`, the figure is displayed in a window. The figure is closed in all cases to release memory.

### Inputs

- **`df`** (`pd.DataFrame`) : Both trajectories, columns `x_theory`/`y_theory` and `x_model`/`y_model`, from `calculate_analytical_trajectory`.
- **`filename`** (`Path`) : Path to save the comparison image to.
- **`silent`** (`bool`) : `False` (default) displays the plot on screen; `True` only writes the file.

### Outputs

- None: the function writes the comparison figure to disk (and displays it when not silent).
