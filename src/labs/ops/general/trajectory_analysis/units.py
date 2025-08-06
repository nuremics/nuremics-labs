from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

from nuremics import Process
from importlib.resources import files
from labs.ops.general.plotting import (
    insert_image_into_plot,
)


@Process.analysis_function
def plot_overall_model_vs_theory(
    output: dict,
    settings: dict,
    filename: str,
    silent: bool = False,
) -> None:
    """
    Generate overall comparative plots of simulated (model) and theoritical trajectories.

    This function loads (x, y) trajectory data from a results file ("results.xlsx")
    and compares the model prediction to the theoretical reference for multiple 
    scenarios.

    Parameters
    ----------
    output : dict (containing output path to analyze for each case)
        Each path should contain a 'results.xlsx' file with the columns:
        - 'x_theory', 'y_theory': Theoretical trajectory coordinates.
        - 'x_model', 'y_model': Model/simulated trajectory coordinates.
    
    settings : dict (containing analysis settings for each case)
        Each entry must contain:
        - 'add'   (bool): Whether to include the case in the plot.
        - 'line'  (str) : Line style used for plotting the model trajectory.
        - 'label' (str) : Label for the legend; if set to "Model", the case name is used.
    
    filename : str
        Path to the file where the generated plot image will be saved (PNG format recommended).
    silent : bool (default is False)
        If False, displays the plot interactively using a window (e.g. for inspection).
    """
    
    # Flag to plot "Theory" label only once
    first = True

    # Define plot
    fig, ax = plt.subplots()
    
    # Browse output for each case
    for case, out in output.items():
        if not settings[case]["add"]:
            continue

        # Load results from Excel file
        df = pd.read_excel(Path(out) / "results.xlsx")

        # Extract line style and label for the case
        color = settings[case]["color"]
        linestyle = settings[case]["linestyle"]
        linewidth = settings[case]["linewidth"]
        marker = settings[case]["marker"]
        markersize = settings[case]["markersize"]
        markerevery = settings[case]["markevery"]
        label = settings[case]["label"]
        if label == "Model":
            label = case
        
        # Plot theoretical trajectory, only label the first one
        if first:
            ax.plot(df["x_theory"], df["y_theory"], "k",
                zorder=3,
                linewidth=linewidth,
                label="Theory",
            )
        else:
            ax.plot(df["x_theory"], df["y_theory"], "k",
                zorder=3,
                linewidth=linewidth,
            )
        
        # Plot model trajectory
        ax.plot(df["x_model"], df["y_model"],
            color=color,
            linestyle=linestyle,
            linewidth=linewidth,
            marker=marker,
            markevery=markerevery,
            markersize=markersize,
            label=label,
            zorder=4,
        )

        first = False
    
    # Set title and axis labels
    ax.set_title("(x, y) trajectory: model vs. theory", fontsize=14)
    ax.set_xlabel("x (m)", fontsize=14)
    ax.set_ylabel("y (m)", fontsize=14)

    # Set equal aspect ratio, legend and grid
    ax.set_aspect("equal", adjustable="datalim")
    ax.autoscale_view()
    ax.legend(
        fontsize=14,
        loc="upper right",
    )
    ax.grid(True)

    # Insert NUREMICS logo in plot background
    insert_image_into_plot(
        img_path=files("nuremics.resources").joinpath("logo.png"),
        fig=fig,
        ax=ax,
        alpha=0.3,
        scale=0.8,
    )

    # Save the plot to the specified file (with high resolution)
    fig.savefig(filename, dpi=300)

    # Display the plot in a window if silent mode is disabled
    if not silent:
        plt.show()
    
    # Close the figure to release memory
    plt.close(fig)