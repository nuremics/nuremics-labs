# PolygonGeometryProc

<p align="left">
  <img src="https://img.shields.io/badge/Pandas-2.2.2+-0b0153?style=flat&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-2.0.1+-4dabcf?style=flat&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/matplotlib-3.10.3+-11557c" />
</p>

## Process

Generate and plot a regular 2D polygon shape.<br>
A/ **`generate_polygon_shape`:** Generate the 2D coordinates of a regular polygon.<br>
B/ **`plot_polygon_shape`:** Plot a closed 2D polygon from a set of points.

```mermaid
erDiagram
  **Parameters** ||--|| **Inputs** : provides
  **Paths** ||--|| **Inputs** : provides
  **Inputs** ||--|| **PolygonGeometryProc** : feeds
  **PolygonGeometryProc** ||--|| **Outputs** : generates

  **Parameters** {
    float radius
    int n_sides
  }
  **Paths** {
    file title_file "txt"
  }
  **PolygonGeometryProc** {
    op generate_polygon_shape
    op plot_polygon_shape
  }
  **Outputs** {
    file coords_file "csv"
    file fig_file "png"
  }
```

## Input Parameter(s)

- **`radius`:** Radius of the polygon.
- **`n_sides`:** Number of sides of the polygon.

## Input Path(s)

- **`title_file`:** File containing the plot title of the 2D polygon shape.

## Output Path(s)

- **`coords_file`:** File containing the X/Y coordinates of the polygon vertices.
- **`fig_file`:** Image of the plotted polygon figure.