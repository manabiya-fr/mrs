from IPython.display import Image, display


def verify_bbox(fig, x0, y0, width, height, filename="/tmp/fig_verify_bbox.png"):
    """Verify a manual bounding box (to be used in jupyterlab)."""
    fig.savefig(
        filename,
        bbox_inches=fig.bbox_inches.from_bounds(x0, y0, width, height),
    )
    display(Image(filename=filename))
