from pathlib import Path
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use("TkAgg")

from nuremics import Process

@Process.analysis_function
def run_analysis(
    output: dict,
    settings: dict,
    filename: str,
    verbose: bool,
) -> None:
    """
    Compare model vs. theoretical (x, y) trajectories.

    This function loads trajectory data from a results file ("results.xlsx")
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
    verbose : bool
        If True, displays the plot interactively using a window (e.g. for inspection).
    """

    manager = plt.get_current_fig_manager()
    manager.window.wm_geometry("+1110+0")
    
    # Flag to plot "Theory" label only once
    first = True
    
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
        
        # Plot theoretical trajectory (black line), only label the first one
        if first:
            plt.plot(df["x_theory"], df["y_theory"], "k",
                zorder=3,
                linewidth=linewidth,
                label="Theory",
            )
        else:
            plt.plot(df["x_theory"], df["y_theory"], "k",
                zorder=3,
                linewidth=linewidth,
            )
        
        # Plot model trajectory
        plt.plot(df["x_model"], df["y_model"],
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
    plt.title("(x, y) trajectory: model vs. theory", fontsize=14)
    plt.xlabel("x (m)", fontsize=14)
    plt.ylabel("y (m)", fontsize=14)
    
    # Add legend and grid
    plt.legend(
        fontsize=14,
        loc="upper right",
    )
    plt.grid(True)

    # Keep aspect ratio equal for visual accuracy
    plt.axis("equal")

    # Save the plot to the specified file (with high resolution)
    plt.savefig(filename, dpi=300)

    # Display the plot in a window if verbose mode is enabled
    if verbose:
        plt.show()
    
    # Close the figure to release memory
    plt.close()