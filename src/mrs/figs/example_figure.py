"""An example figure."""

import matplotlib.pyplot as plt
import numpy as np


def generate(filename=None):
    axis_limit = 1.2
    arrow_length_ratio = 0.07
    scale = 1.04
    fontsize = 14
    v = np.array([1, 1, 1]) / 2
    origin = np.zeros(3)

    ticks = np.linspace(0, axis_limit, 5)
    axlim = [0, axis_limit]

    axes_data = [
        (np.array([1, 0, 0]), r"$x$", "r"),
        (np.array([0, 1, 0]), r"$y$", "g"),
        (np.array([0, 0, 1]), r"$z$", "b"),
        (np.array([1 / 2, 1 / 2, 1 / 2]), r"$\mathcal{V}$", "k"),
    ]

    fig = plt.figure(figsize=(6, 6))
    ax = plt.axes(projection="3d")

    for vec, label, color in axes_data:
        ax.quiver(*origin, *vec, color=color, arrow_length_ratio=arrow_length_ratio)
        ax.text(*(vec * scale), label, color=color, fontsize=fontsize)

    ax.set_xticklabels([])
    ax.set_yticklabels([])
    ax.set_zticklabels([])

    ax.set_xticks(ticks)
    ax.set_yticks(ticks)
    ax.set_zticks(ticks)

    ax.set_xlim(axlim)
    ax.set_ylim(axlim)
    ax.set_zlim(axlim)

    ax.set_box_aspect([1, 1, 1])

    ax.view_init(elev=15, azim=-60)
    ax.set_axis_off()

    if filename is not None:
        fig.savefig(
            filename,
            backend="pgf",
            transparent=True,
            bbox_inches=fig.bbox_inches.from_bounds(1.15, 1.05, 2.4, 3.0),
        )
    else:
        return fig


if __name__ == "__main__":
    generate("out/example.pgf")
