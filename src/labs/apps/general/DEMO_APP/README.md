# DEMO_APP

<p align="left">
  <img src="https://img.shields.io/badge/Pandas-2.2.2+-0b0153?style=flat&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-2.0.1+-4dabcf?style=flat&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/matplotlib-3.10.3+-11557c" />
  <img src="https://img.shields.io/badge/pygame-2.6.1+-08df1c" />
  <img src="https://img.shields.io/badge/pymunk-7.0.1+-3398da" />
  <img src="https://img.shields.io/badge/XlsxWriter-3.2.3+-207346" />
  <img src="https://img.shields.io/badge/openpyxl-3.1.5+-010043" />
</p>

## Workflow

1. **`PolygonGeometryProc`:** Generate and plot a regular 2D polygon shape.<br>
  A/ **`generate_polygon_shape`:** Generate the 2D coordinates of a regular polygon.<br>
  B/ **`plot_polygon_shape`:** Plot a closed 2D polygon from a set of points.
2. **`ProjectileModelProc`:** Simulate the motion of a projectile and compare its trajectory with the analytical solution.<br>
  A/ **`simulate_projectile_motion`:** Simulate the motion of a 2D rigid body under gravity projected with an initial velocity.<br>
  B/ **`calculate_analytical_trajectory`:** Calculate the theoretical trajectory of a projectile using analytical equations.<br>
  C/ **`compare_model_vs_analytical_trajectories`:** Plot and save the comparison between simulated (model) and theoretical projectile trajectories.
3. **`TrajectoryAnalysisProc`:** Perform overall comparisons between simulated (model) and theoretical trajectories.<br>
  A/ **`plot_overall_model_vs_theory`:** Generate overall comparative plots of simulated (model) and theoritical trajectories.

```mermaid
flowchart RL
  **PolygonGeometryProc** e1@--1--o **DEMO_APP**
  **ProjectileModelProc** e2@--2--o **DEMO_APP**
  **TrajectoryAnalysisProc** e3@--3--o **DEMO_APP**
  **generate_polygon_shape** e4@--A--o **PolygonGeometryProc**
  **plot_polygon_shape** e5@--B--o **PolygonGeometryProc**
  **simulate_projectile_motion** e6@--A--o **ProjectileModelProc**
  **calculate_analytical_trajectory** e7@--B--o **ProjectileModelProc**
  **compare_model_vs_analytical_trajectories** e8@--C--o **ProjectileModelProc**
  **plot_overall_model_vs_theory** e9@--A--o **TrajectoryAnalysisProc**
  e1@{ animate: true }
  e2@{ animate: true }
  e3@{ animate: true }
  e4@{ animate: true }
  e5@{ animate: true }
  e6@{ animate: true }
  e7@{ animate: true }
  e8@{ animate: true }
  e9@{ animate: true }
```

## Mapping

```mermaid
erDiagram
  **DEMO_APP** ||--|| **user_params** : mapping
  **DEMO_APP** ||--|| **hard_params** : mapping
  **DEMO_APP** ||--|| **user_paths** : mapping
  **DEMO_APP** ||--|| **output_paths** : mapping
  **user_params** ||--|| **PolygonGeometryProc** : mapping
  **hard_params** ||--|| **PolygonGeometryProc** : mapping
  **user_paths** ||--|| **PolygonGeometryProc** : mapping
  **output_paths** ||--|| **PolygonGeometryProc** : mapping

  **user_params** {
    int n_sides "nb_sides"
  }
  **hard_params** {
    float radius "0.5"
  }
  **user_paths** {
    file title_file "plot_title.txt"
  }
  **output_paths** {
    file coords_file "points_coordinates.csv"
    file fig_file "polygon_shape.png"
  }
```

```mermaid
erDiagram
  **DEMO_APP** ||--|| **user_params** : mapping
  **DEMO_APP** ||--|| **user_paths** : mapping
  **DEMO_APP** ||--|| **required_paths** : mapping
  **DEMO_APP** ||--|| **output_paths** : mapping
  **user_params** ||--|| **ProjectileModelProc** : mapping
  **user_paths** ||--|| **ProjectileModelProc** : mapping
  **required_paths** ||--|| **ProjectileModelProc** : mapping
  **output_paths** ||--|| **ProjectileModelProc** : mapping

  **user_params** {
    float gravity "gravity"   
    float mass "mass"
  }
  **user_paths** {
    file velocity_file "velocity.json"
    folder configs_folder "configs"
  }
  **required_paths** {
    file coords_file "points_coordinates.csv"
  }
  **output_paths** {
    folder comp_folder "comparison"
  }
```

```mermaid
erDiagram
  **DEMO_APP** ||--|| **overall_analysis** : mapping
  **DEMO_APP** ||--|| **output_paths** : mapping
  **overall_analysis** ||--|| **TrajectoryAnalysisProc** : mapping
  **output_paths** ||--|| **TrajectoryAnalysisProc** : mapping

  **overall_analysis** {
    folder comp_folder "comparison"
  }
  **output_paths** {
    file fig_file "overall_comparisons.png" 
  }
```

## I/O Interface

```mermaid
flowchart LR
  subgraph **INPUTS**
    direction TB

    subgraph **Paths**
      direction LR
      path1["plot_title.txt _(file)_"]
      path2["velocity.json _(file)_"]
      path3["configs _(folder)_"]
    end

    subgraph **Parameters**
      direction LR
      param1["nb_sides _(int)_"]
      param2["gravity _(float)_"]
      param3["mass _(float)_"]
    end
  end

  subgraph **DEMO_APP**
    direction RL
    proc1["PolygonGeometryProc"]
    proc2["ProjectileModelProc"]
    proc3["TrajectoryAnalysisProc"]
  end

  subgraph **OUTPUTS**
    direction RL
    out1["points_coordinates.csv _(file)_"]
    out2["polygon_shape.png _(file)_"]
    out3["comparison _(folder)_"]
    out4["overall_comparisons.png _(file)_"]
  end

  **INPUTS** --> **DEMO_APP**
  **DEMO_APP** --> **OUTPUTS**
```

```mermaid
flowchart LR
  subgraph **INPUTS**
    direction TB

    subgraph **Paths**
      direction LR
      path1["plot_title.txt _(file)_"]
    end

    subgraph **Parameters**
      direction LR
      param1["nb_sides _(int)_"]
    end
  end

  subgraph **DEMO_APP**
    direction RL
    proc1["PolygonGeometryProc"]
  end

  subgraph **OUTPUTS**
    direction RL
    out1["points_coordinates.csv _(file)_"]
    out2["polygon_shape.png _(file)_"]
  end

  **INPUTS** --> proc1
  proc1 --> **OUTPUTS**
```

```mermaid
flowchart LR
  subgraph **INPUTS**
    direction TB

    subgraph **Paths**
      direction LR
      path2["velocity.json _(file)_"]
      path3["configs _(folder)_"]
      out1["points_coordinates.csv _(file)_"]
    end

    subgraph **Parameters**
      direction LR
      param2["gravity _(float)_"]
      param3["mass _(float)_"]
    end
  end

  subgraph **DEMO_APP**
    direction RL
    proc2["ProjectileModelProc"]
  end

  subgraph **OUTPUTS**
    direction RL
    out3["comparison _(folder)_"]
  end

  **INPUTS** --> proc2
  proc2 --> **OUTPUTS**

  classDef blueBox fill:#d0e6ff,stroke:#339,stroke-width:1.5px;
  class out1 blueBox;
```

```mermaid
flowchart LR
  subgraph **INPUTS**
    direction TB

    subgraph **Paths**
      direction LR
      out3["comparison _(folder)_"]
    end

    subgraph **Parameters**
      direction LR
      param["_"]
    end
  end

  subgraph **DEMO_APP**
    direction RL
    proc3["TrajectoryAnalysisProc"]
  end

  subgraph **OUTPUTS**
    direction RL
    out4["overall_comparisons.png _(file)_"]
  end

  **INPUTS** --> proc3
  proc3 --> **OUTPUTS**

  classDef blueBox fill:#d0e6ff,stroke:#339,stroke-width:1.5px;
  class out3 blueBox;
```

### INPUTS

#### Parameters

- **`nb_sides`:** Number of sides of the polygon.
- **`gravity`:** Gravitational acceleration (m/s²).
- **`mass`:** Mass of the body (kg).

#### Paths

- **`plot_title.txt`:** File containing the plot title of the 2D polygon shape.
- **`velocity.json`:** File containing the velocity initial conditions {v0 (m/s); angle (°)}.
- **`configs/`** <br>
  **`solver_config.json`:** File containing the parameters for solver configuration. <br>
  **`display_config.json`:** File containing the parameters for display configuration.

### OUTPUTS

- **`points_coordinates.csv`:** File containing the X/Y coordinates of the polygon vertices.
- **`polygon_shape.png`:** Image of the plotted polygon figure.
- **`comparison/`** <br>
  **`results.xlsx`:** File containing simulated (model) and theoritical trajectories. <br>
  **`model_vs_theory.png`:** Image comparing both trajectories.
- **`overall_comparisons.png`:** Image containing overall comparative plots.