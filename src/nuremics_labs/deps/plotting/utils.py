import matplotlib.image as mpimg
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from PIL import Image


def insert_image_into_plot(
    img_path: str,
    fig: Figure,
    ax: Axes,
    alpha: float = 0.5,
    scale: float = 1.0,
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

    # Force figure canvas to render so that axis limits are updated
    fig.canvas.draw()

    # Get current axis limits (bounding box of the plot area)
    xmin_plot, xmax_plot = ax.get_xlim()
    ymin_plot, ymax_plot = ax.get_ylim()

    # Re-apply axis limits to prevent matplotlib from auto-scaling after drawing the image
    ax.set_xlim(xmin_plot, xmax_plot)
    ax.set_ylim(ymin_plot, ymax_plot)

    # Calculate width, height and aspect ratio of the plot area
    w_plot = xmax_plot - xmin_plot
    h_plot = ymax_plot - ymin_plot
    r_plot = h_plot / w_plot  # aspect ratio of the plot

    # Load image with PIL to get its native width and height
    img_pil = Image.open(img_path)
    w_img, h_img = img_pil.size
    r_img = h_img / w_img  # aspect ratio of the image

    # Determine how to scale and position the image based on aspect ratios
    if abs(r_img - r_plot) < 1e-8:
        # Image and plot have same aspect ratio: fill entire plot area
        w_img_target = w_plot
        h_img_target = h_plot

    elif r_img < r_plot:
        # Image is relatively wider than plot → scale image width to plot width
        w_img_target = w_plot
        h_img_target = r_img * w_img_target  # adjust height to preserve ratio

    else:
        # Image is relatively taller than plot → scale image height to plot height
        h_img_target = h_plot
        w_img_target = h_img_target / r_img  # adjust width to preserve ratio

    # Apply the scale factor to computed target size
    w_img_target *= scale
    h_img_target *= scale

    # Compute centered coordinates of the image inside the plot limits
    x_center = (xmin_plot + xmax_plot) / 2
    y_center = (ymin_plot + ymax_plot) / 2

    xmin_img = x_center - w_img_target / 2
    xmax_img = x_center + w_img_target / 2
    ymin_img = y_center - h_img_target / 2
    ymax_img = y_center + h_img_target / 2

    # Load image as an array for matplotlib display
    img = mpimg.imread(img_path)

    # Display the image with calculated extent and transparency
    ax.imshow(
        img,
        extent=[xmin_img, xmax_img, ymin_img, ymax_img],
        zorder=0,  # ensure image is drawn behind plot elements
        alpha=alpha,
    )