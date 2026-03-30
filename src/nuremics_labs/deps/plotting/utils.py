from importlib.resources import files

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from PIL import Image


def insert_image_into_plot(
    img_path: str,
    fig: Figure,
    ax: Axes,
    alpha: float = 0.3,
    scale: float = 0.8,
) -> None:
    """
    Insert an image into a matplotlib Axes, preserving its aspect ratio and plot limits.

    Parameters
    ----------
    img_path : str
        Path to the image file.
    fig : Figure
        Matplotlib Figure object (used to force rendering).
    ax : Axes
        Matplotlib Axes where the image will be inserted.
    alpha : float, optional
        Transparency level of the image, by default 0.5.
    scale : float, optional
        Scaling factor for the image size relative to fitted size (default is 1.0).
        Values < 1 reduce size, > 1 enlarge.
    """

    # Force rendering to update axis limits and bounding box
    fig.canvas.draw()

    xmin_plot, xmax_plot = ax.get_xlim()
    ymin_plot, ymax_plot = ax.get_ylim()

    # Physical size of the axes in pixels
    bbox = ax.get_window_extent()
    w_display = bbox.width
    h_display = bbox.height

    # Data ranges
    w_data = xmax_plot - xmin_plot
    h_data = ymax_plot - ymin_plot

    # Scale factors: pixels per data unit
    sx = w_display / w_data  # pixels / X unit
    sy = h_display / h_data  # pixels / Y unit

    # Native aspect ratio of the image (in pixels)
    img_pil = Image.open(img_path)
    w_img, h_img = img_pil.size
    r_img = h_img / w_img

    # To display the image without distortion:
    #   (h_extent * sy) / (w_extent * sx) == r_img
    # => h_extent / w_extent == r_img * (sx / sy)   [target ratio in data coords]
    r_target = r_img * (sx / sy)

    # Compute extent in data coords, fitting within the plot area
    w_extent = w_data
    h_extent = r_target * w_data

    if h_extent > h_data:  # too tall → constrain by height
        h_extent = h_data
        w_extent = h_data / r_target

    # Apply scale factor
    w_extent *= scale
    h_extent *= scale

    # Center the image within the plot area
    x_center = (xmin_plot + xmax_plot) / 2
    y_center = (ymin_plot + ymax_plot) / 2

    xmin_img = x_center - w_extent / 2
    xmax_img = x_center + w_extent / 2
    ymin_img = y_center - h_extent / 2
    ymax_img = y_center + h_extent / 2

    # Re-apply axis limits to prevent imshow from modifying them
    ax.set_xlim(xmin_plot, xmax_plot)
    ax.set_ylim(ymin_plot, ymax_plot)

    # Save current aspect setting before imshow overrides it
    current_aspect = ax.get_aspect()

    img = mpimg.imread(img_path)
    ax.imshow(
        img,
        extent=[xmin_img, xmax_img, ymin_img, ymax_img],
        zorder=0,
        alpha=alpha,
        aspect="auto",  # let matplotlib handle aspect ratio based on extent
    )

    # Restore the original aspect setting (e.g. "equal") that imshow may have overridden
    ax.set_aspect(current_aspect)


def plot_xy(
    list_plots: list,
    config: tuple,
    size: tuple,
    logo: bool = True,
    save_pdf: str = None,
    save_png: str = None,
) -> None:

    fig, ax = plt.subplots(config[0], config[1])
    ax = np.atleast_1d(ax).ravel()
    fig.set_size_inches(size[0], size[1])

    for i, plot in enumerate(list_plots):
        
        x_column = plot["x_column"]
        y_column = plot["y_column"]
        title = plot["title"]
        x_label = plot["x_label"]
        y_label = plot["y_label"]
        marker = plot["marker"]
        linestyle = plot["linestyle"]
        linewidth = plot["linewidth"]
        color = plot["color"]
        label = plot["label"]
        zorder = plot["zorder"]

        for j, df in enumerate(plot["df"]):
        
            x_data = df[x_column[j]]
            y_data = df[y_column[j]]

            if label is not None:
                this_label = label[j]
            else:
                this_label = label

            if marker is not None:
                this_marker = marker[j]
            else:
                this_marker = marker

            if linestyle is not None:
                this_linestyle = linestyle[j]
            else:
                this_linestyle = linestyle

            if linewidth is not None:
                this_linewidth = linewidth[j]
            else:
                this_linewidth = linewidth
            
            if color is not None:
                this_color = color[j]
            else:
                this_color = color
            
            if zorder is not None:
                this_zorder = zorder[j]
            else:
                this_zorder = zorder
        
            ax[i].plot(x_data, y_data,
                marker=this_marker,
                linestyle=this_linestyle,
                linewidth=this_linewidth,
                color=this_color,
                label=this_label,
                zorder=this_zorder,
            )

        if title is not None:
            ax[i].set_title(title)
        if x_label is not None:
            ax[i].set_xlabel(x_label)
        if y_label is not None:
            ax[i].set_ylabel(y_label)
        ax[i].grid(True)

        # Check if a legend label is provided
        if label is not None:
            ax[i].legend()  # Display the legend if a label is given
            ax[i].legend(
                loc="center left",
                bbox_to_anchor=(1, 0.5)
            )

        # Insert nuRemics logo in plot background
        if logo:
            insert_image_into_plot(
                img_path=files("nuremics.resources").joinpath("logo.png"),
                fig=fig,
                ax=ax[i],
                alpha=0.3,
                scale=0.8,
            )

    # Save the plot as a PDF if save_pdf is specified
    if save_pdf is not None:
        plt.savefig(save_pdf, format="pdf")
    
    # Save the plot as a PNG if save_png is specified
    if save_png is not None:
        plt.savefig(save_png,
            format="png",
            dpi=300,
            bbox_inches="tight",
        )
    
    plt.close()