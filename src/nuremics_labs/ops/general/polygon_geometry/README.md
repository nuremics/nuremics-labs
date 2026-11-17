# polygon_geometry — ops

## Functions

- `generate_polygon_shape`
- `plot_polygon_shape`

---

## `generate_polygon_shape`

### Overview

Compute the vertex coordinates of a regular polygon centered at the origin.

### Description

Computes the `n_sides` vertices of a regular polygon on its circumscribed circle of the given `radius`, counter-clockwise starting from angle zero, and assembles them into a DataFrame with the columns `X` and `Y` (meters, polygon centered at the origin). When `filename` is provided, the coordinates are saved to that CSV file. The polygon is returned counter-clockwise, ready for plotting or for use as a rigid-body cross-section.

### Inputs

- **`radius`** (`float`) : Radius (m) of the circumscribed circle of the polygon.
- **`n_sides`** (`int`) : Number of sides of the polygon.
- **`filename`** (`Optional[str]`) : CSV file to write the coordinates to; skipped when `None`.

### Outputs

- **`df_points`** (`pd.DataFrame`) : Vertex coordinates of the polygon, columns `X` and `Y`, counter-clockwise, centered at the origin.

---

## `plot_polygon_shape`

### Overview

Plot a closed 2D polygon from a set of points and save the figure.

### Description

Closes the polygon by appending its first vertex at the end of the point list, then plots the closed line in its fixed style (blue line, round markers). The title, the axis labels (`x (m)`, `y (m)`), an equal aspect ratio and a grid are applied, the nuRemics logo is inserted in the plot background, and the figure is saved to `filename` at 300 dpi. When `silent` is `False`, the figure is displayed in a window. The figure is closed in all cases to release memory.

### Inputs

- **`df_points`** (`pd.DataFrame`) : Vertex coordinates of the polygon, columns `X` and `Y`.
- **`title`** (`str`) : Title of the plot.
- **`filename`** (`str`) : Path to save the plot image to (e.g. `shape.png`).
- **`silent`** (`bool`) : `False` (default) displays the plot on screen; `True` only writes the file.

### Outputs

- None: the function writes the figure to disk (and displays it when not silent).
