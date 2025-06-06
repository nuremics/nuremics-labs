## Diagram

```mermaid
flowchart BT
  **OneProc** e1@--1--o **ONE_APP**
  **AnotherProc** e2@--2--o **ONE_APP**
  **AnalysisProc** e3@--3--o **ONE_APP**
  e1@{ animate: true }
  e2@{ animate: true }
  e3@{ animate: true }
```

## Description

Simulate a projectile trajectory and compare it with the analytical solution.

## Workflow

1. **`OneProc`:** Generate and plot a regular polygon shape.
2. **`AnotherProc`:** Simulate a projectile trajectory and compare it with the analytical solution.
3. **`AnalysisProc`:** Plot and save the comparison between simulated and theoretical trajectories.

## Mapping

```mermaid
erDiagram
  **ONE_APP** ||--|| **user_params** : mapping
  **ONE_APP** ||--|| **hard_params** : mapping
  **ONE_APP** ||--|| **user_paths** : mapping
  **ONE_APP** ||--|| **output_paths** : mapping
  **user_params** ||--|| **OneProc** : mapping
  **hard_params** ||--|| **OneProc** : mapping
  **user_paths** ||--|| **OneProc** : mapping
  **output_paths** ||--|| **OneProc** : mapping

  **user_params** {
    int param2 "parameter1"
  }
  **hard_params** {
    float param1 "0.5"
  }
  **user_paths** {
    file path1 "input1.txt"
  }
  **output_paths** {
    file out1 "output1.csv"
    file out2 "output2.png"
  }
```

```mermaid
erDiagram
  **ONE_APP** ||--|| **user_params** : mapping
  **ONE_APP** ||--|| **user_paths** : mapping
  **ONE_APP** ||--|| **required_paths** : mapping
  **ONE_APP** ||--|| **output_paths** : mapping
  **user_params** ||--|| **AnotherProc** : mapping
  **user_paths** ||--|| **AnotherProc** : mapping
  **required_paths** ||--|| **AnotherProc** : mapping
  **output_paths** ||--|| **AnotherProc** : mapping

  **user_params** {
    float param1 "parameter2"
    float param2 "parameter3"
  }
  **user_paths** {
    file path1 "input2.json"
    folder path2 "input3"
  }
  **required_paths** {
    file path3 "output1.csv"
  }
  **output_paths** {
    folder out1 "output3"
  }
```

```mermaid
erDiagram
  **ONE_APP** ||--|| **output_paths** : mapping
  **ONE_APP** ||--|| **overall_analysis** : mapping
  **output_paths** ||--|| **AnalysisProc** : mapping
  **overall_analysis** ||--|| **AnalysisProc** : mapping

  **output_paths** {
    file out1 "output4.png"
  }
  **overall_analysis** {
    folder analysis1 "output3"
  }
```

## I/O Interface

```mermaid
flowchart LR
  subgraph **INPUTS**
    direction TB

    subgraph **Paths**
      direction LR
      path1["input1.txt _(file)_"]
      path2["input2.json _(file)_"]
      path3["input3 _(folder)_"]
    end

    subgraph **Parameters**
      direction LR
      param1["parameter1 _(int)_"]
      param2["parameter2 _(float)_"]
      param3["parameter3 _(float)_"]
    end
  end

  subgraph **OUTPUTS**
    direction RL
    out1["output1.csv _(file)_"]
    out2["output2.png _(file)_"]
    out3["output3 _(folder)_"]
    out4["output4.png _(file)_"]
  end

  **INPUTS** --> ONE_APP["**ONE_APP**"]
  ONE_APP --> **OUTPUTS**
```

### INPUTS

#### Parameters

- **`parameter1`:** Number of sides of the polygon.
- **`parameter2`:** Acceleration due to gravity (can be positive or negative).
- **`parameter3`:** Mass of the projectile (used in the simulation).

#### Paths

- **`input1.txt`:** File containing the plot title.
- **`input2.json`:** File containing initial conditions (v0, h0, angle).
- **`input3/`** 
  - **`solver_config.json`:** File containing the parameters for solver configuration.
  - **`display_config.json`:** File containing the parameters for display configuration.

### OUTPUTS

- **`output1.csv`:** File containing the X/Y coordinates of the polygon vertices.
- **`output2.png`:** Image of the plotted polygon figure.
- **`output3/`**
  - **`results.xlsx`:** File containing model and theoritical trajectories.
  - **`model_vs_theory.png`:** Image comparing both trajectories.
- **`output4.png`:** Image comparing both trajectories across all experiments.