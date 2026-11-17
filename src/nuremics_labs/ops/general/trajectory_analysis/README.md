# trajectory_analysis — ops

## Functions

- `plot_overall_model_vs_theory`

---

## `plot_overall_model_vs_theory`

### Overview

Assemble the model-vs-theory comparison of every case into one overall plot.

### Description

Framework analysis function (registered with `Process.analysis_function`): iterates the output path of every case, skips the cases whose settings exclude them (`add` is `False`), reads each case spreadsheet (`results.xlsx`, columns `t`, `x_theory`, `y_theory`, `x_model`, `y_model`), and plots in the same axes the theoretical trajectory as a black line (legend `Theory`, labeled only for the first included case) and the simulated trajectory of each case styled by its settings (`color`, `linestyle`, `linewidth`, `marker`, `markersize`, `markevery`, `label`; an empty label falls back to the case name). The title `(x, y) trajectory: model vs. theory`, the axis labels (`x (m)`, `y (m)`), an equal aspect ratio, an upper-right legend and a grid are applied, the nuRemics logo is inserted in the plot background, and the figure is saved to `filename` at 300 dpi. When `silent` is `False`, the figure is displayed in a window. The figure is closed in all cases to release memory.

### Inputs

- **`output`** (`dict`) : Output path to analyze for each case, each holding a `results.xlsx` spreadsheet from `calculate_analytical_trajectory`.
- **`settings`** (`dict`) : Analysis settings for each case: `add` (`bool`, include the case), `color`, `linestyle`, `linewidth`, `marker`, `markersize`, `markevery`, `label` (`str`, legend label; empty falls back to the case name).
- **`filename`** (`str`) : Path to save the overall plot image to.
- **`silent`** (`bool`) : `False` (default) displays the plot on screen; `True` only writes the file.

### Outputs

- None: the function writes the overall figure to disk (and displays it when not silent).
