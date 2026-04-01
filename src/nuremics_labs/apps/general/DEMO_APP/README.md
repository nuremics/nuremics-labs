# DEMO_APP

<p align="left">
  <img src="https://img.shields.io/badge/Pandas-2.1.1+-0b0153?style=flat&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-1.26.0+-4dabcf?style=flat&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/matplotlib-3.9.4+-11557c" />
  <img src="https://img.shields.io/badge/pygame-2.6.1+-08df1c" />
  <img src="https://img.shields.io/badge/pymunk-7.0.1+-3398da" />
  <img src="https://img.shields.io/badge/XlsxWriter-3.2.3+-207346" />
  <img src="https://img.shields.io/badge/openpyxl-3.1.5+-010043" />
</p>

## Workflow

1. **[`PolygonGeometryProc`](https://github.com/nuremics/nuremics-labs/tree/main/src/nuremics_labs/procs/general/PolygonGeometryProc):** Generate and plot a regular 2D polygon shape.<br>
  A/ **`generate_polygon_shape`:** Generate the 2D coordinates of a regular polygon.<br>
  B/ **`plot_polygon_shape`:** Plot a closed 2D polygon from a set of points.
2. **[`ProjectileModelProc`](https://github.com/nuremics/nuremics-labs/tree/main/src/nuremics_labs/procs/general/ProjectileModelProc):** Simulate the motion of a projectile and compare its trajectory with the analytical solution.<br>
  A/ **`simulate_projectile_motion`:** Simulate the motion of a 2D rigid body under gravity projected with an initial velocity.<br>
  B/ **`calculate_analytical_trajectory`:** Calculate the theoretical trajectory of a projectile using analytical equations.<br>
  C/ **`compare_model_vs_analytical_trajectories`:** Plot and save the comparison between simulated (model) and theoretical projectile trajectories.
3. **[`TrajectoryAnalysisProc`](https://github.com/nuremics/nuremics-labs/tree/main/src/nuremics_labs/procs/general/TrajectoryAnalysisProc):** Perform overall comparisons between simulated (model) and theoretical trajectories.<br>
  A/ **`plot_overall_model_vs_theory`:** Generate overall comparative plots of simulated (model) and theoritical trajectories.

```mermaid
flowchart RL
  Proc1[<b>PolygonGeometryProc<b>] e1@--1--o App[<b>DEMO_APP<b>]
  Proc2[<b>ProjectileModelProc<b>] e2@--2--o App
  Proc3[<b>TrajectoryAnalysisProc<b>] e3@--3--o App
  Op11[<b>generate_polygon_shape<b>] e4@--A--o Proc1
  Op12[<b>plot_polygon_shape<b>] e5@--B--o Proc1
  Op21[<b>simulate_projectile_motion<b>] e6@--A--o Proc2
  Op22[<b>calculate_analytical_trajectory<b>] e7@--B--o Proc2
  Op23[<b>compare_model_vs_analytical_trajectories<b>] e8@--C--o Proc2
  Op31[<b>plot_overall_model_vs_theory<b>] e9@--A--o Proc3
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
  subgraph Inputs[<b>INPUTS<b>]
    direction TB

    subgraph Paths[<b>Paths<b>]
      direction LR
      path1["plot_title.txt <i>(file)<i>"]
      path2["velocity.json <i>(file)<i>"]
      path3["configs <i>(folder)<i>"]
    end

    subgraph Parameters[<b>Parameters<b>]
      direction LR
      param1["nb_sides <i>(int)<i>"]
      param2["gravity <i>(float)<i>"]
      param3["mass <i>(float)<i>"]
    end
  end

  subgraph App[<b>DEMO_APP<b>]
    direction RL
    proc1["PolygonGeometryProc"]
    proc2["ProjectileModelProc"]
    proc3["TrajectoryAnalysisProc"]
  end

  subgraph Outputs[<b>OUTPUTS<b>]
    direction RL
    out1["points_coordinates.csv <i>(file)<i>"]
    out2["polygon_shape.png <i>(file)<i>"]
    out3["comparison <i>(folder)<i>"]
    out4["overall_comparisons.png <i>(file)<i>"]
  end

  Inputs --> App
  App --> Outputs
```

```mermaid
flowchart LR
  subgraph Inputs[<b>INPUTS<b>]
    direction TB

    subgraph Paths[<b>Paths<b>]
      direction LR
      path1["plot_title.txt <i>(file)<i>"]
    end

    subgraph Parameters[<b>Parameters<b>]
      direction LR
      param1["nb_sides <i>(int)<i>"]
    end
  end

  subgraph App[<b>DEMO_APP<b>]
    direction RL
    proc1["PolygonGeometryProc"]
  end

  subgraph Outputs[<b>OUTPUTS<b>]
    direction RL
    out1["points_coordinates.csv <i>(file)<i>"]
    out2["polygon_shape.png <i>(file)<i>"]
  end

  Inputs --> proc1
  proc1 --> Outputs
```

```mermaid
flowchart LR
  subgraph Inputs[<b>INPUTS<b>]
    direction TB

    subgraph Paths[<b>Paths<b>]
      direction LR
      path2["velocity.json <i>(file)<i>"]
      path3["configs <i>(folder)<i>"]
      out1["points_coordinates.csv <i>(file)<i>"]
    end

    subgraph Parameters[<b>Parameters<b>]
      direction LR
      param2["gravity <i>(float)<i>"]
      param3["mass <i>(float)<i>"]
    end
  end

  subgraph App[<b>DEMO_APP<b>]
    direction RL
    proc2["ProjectileModelProc"]
  end

  subgraph Outputs[<b>OUTPUTS<b>]
    direction RL
    out3["comparison <i>(folder)<i>"]
  end

  Inputs --> proc2
  proc2 --> Outputs

  classDef blueBox fill:#d0e6ff,stroke:#339,stroke-width:1.5px;
  class out1 blueBox;
```

```mermaid
flowchart LR
  subgraph Inputs[<b>INPUTS<b>]
    direction TB

    subgraph Paths[<b>Paths<b>]
      direction LR
      out3["comparison <i>(folder)<i>"]
    end

    subgraph Parameters[<b>Parameters<b>]
      direction LR
      param["_"]
    end
  end

  subgraph App[<b>DEMO_APP<b>]
    direction RL
    proc3["TrajectoryAnalysisProc"]
  end

  subgraph Outputs[<b>OUTPUTS<b>]
    direction RL
    out4["overall_comparisons.png <i>(file)<i>"]
  end

  Inputs --> proc3
  proc3 --> Outputs

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