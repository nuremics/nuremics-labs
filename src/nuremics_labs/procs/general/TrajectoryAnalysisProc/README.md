# TrajectoryAnalysisProc

<p align="left">
  <img src="https://img.shields.io/badge/Pandas-2.1.1+-0b0153?style=flat&logo=pandas&logoColor=white" />
  <img src="https://img.shields.io/badge/matplotlib-3.9.4+-11557c" />
  <img src="https://img.shields.io/badge/openpyxl-3.1.5+-010043" />
</p>

## Process

Perform overall comparisons between simulated (model) and theoretical trajectories.<br>
A/ **`plot_overall_model_vs_theory`:** Generate overall comparative plots of simulated (model) and theoritical trajectories.

```mermaid
erDiagram
  **Analysis** ||--|| **Inputs** : provides
  **Inputs** ||--|| **TrajectoryAnalysisProc** : feeds
  **TrajectoryAnalysisProc** ||--|| **Outputs** : generates

  **Analysis** {
    folder comp_folder "_"
  }
  **TrajectoryAnalysisProc** {
    op plot_overall_model_vs_theory
  }
  **Outputs** {
    file fig_file "png"
  }
```

## Input Analysis

- **`comp_folder/`**<br>
  **`results.xlsx`:** File containing both trajectories.

## Output Path(s)

- **`fig_file`:** Image containing overall comparative plots.