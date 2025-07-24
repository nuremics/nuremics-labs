# ProjectileModelProc

<p align="left">
  <img src="https://img.shields.io/badge/Pandas-2.2.2+-0b0153?style=flat&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/NumPy-2.0.1+-4dabcf?style=flat&logo=numpy&logoColor=white" />
  <img src="https://img.shields.io/badge/matplotlib-3.10.3+-11557c" />
  <img src="https://img.shields.io/badge/pygame-2.6.1+-08df1c" />
  <img src="https://img.shields.io/badge/pymunk-7.0.1+-3398da" />
  <img src="https://img.shields.io/badge/XlsxWriter-3.2.3+-207346" />
</p>

## Process

Simulate projectile motion and compare its trajectory with the analytical solution.<br>
A/ **`simulate_projectile_motion`:** Simulate the motion of a 2D rigid body under gravity projected with an initial velocity.<br>
B/ **`calculate_analytical_trajectory`:** Calculate the theoretical trajectory of a projectile using analytical equations.<br>
C/ **`compare_model_vs_analytical_trajectories`:** Plot and save the comparison between simulated (model) and theoretical projectile trajectories.

```mermaid
erDiagram
  **Parameters** ||--|| **Inputs** : provides
  **Paths** ||--|| **Inputs** : provides
  **Inputs** ||--|| **ProjectileModelProc** : feeds
  **ProjectileModelProc** ||--|| **Outputs** : generates

  **Parameters** {
    float gravity
    float mass
  }
  **Paths** {
    file velocity_file "json"
    folder configs_folder "_"
    file coords_file "csv"
  }
  **ProjectileModelProc** {
    op simulate_projectile_motion
    op calculate_analytical_trajectory
    op compare_model_vs_analytical_trajectories
  }
  **Outputs** {
    folder comp_folder "_"
  }
```

## Input Parameter(s)

- **`gravity`:** Acceleration due to gravity (can be positive or negative).
- **`mass`:** Mass of the projectile.

## Input Path(s)

- **`velocity_file`:** File containing the velocity initial conditions (v0, angle).
- **`configs_folder/`**<br>
  **`solver_config.json`:** File containing the parameters for solver configuration.<br>
  **`display_config.json`:** File containing the parameters for display configuration.
- **`coords_file`:** File containing the X/Y coordinates of the polygonal shape to simulate.

## Output Path(s)

- **`comp_folder/`**<br>
  **`results.xlsx`:** File containing simulated (model) and theoritical trajectories.<br>
  **`model_vs_theory.png`:** Image comparing both trajectories.