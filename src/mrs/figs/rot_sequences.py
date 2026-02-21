"""Demo of sequences of rotations.

FIXME: include a high-level explanation of what is it that we are demonstrating.

"""

import argparse
from typing import Optional

import numpy as np
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d.axes3d import Axes3D

from mrs.frames import RotationMatrix


def get_parser() -> argparse.ArgumentParser:
    """Return argument parser."""
    parser = argparse.ArgumentParser(description="Sequences of rotations.")
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument(
        "--fixed-frame", action="store_true", help="XYZ around fixed frame."
    )

    group.add_argument(
        "--current-frame", action="store_true", help="ZYX around current frame."
    )

    return parser


def show_seq_rot(
    stages: RotationMatrix | tuple[RotationMatrix, float],
    ax: Optional[Axes3D] = None,
) -> Axes3D:
    """Visualize a sequecne of rotations.

    When an element of ``stages`` is a tuple, the second element is an aoffset along the
    x-axis.

    """
    stages_with_offsets = [
        (stage, 0) if isinstance(stage, RotationMatrix) else stage for stage in stages
    ]

    label_offset = 1.1
    for stage, offset_x in stages_with_offsets:
        offset = [offset_x, 0, 0]
        if ax is None:
            ax = stage.plot(offset, label_offset=label_offset)
        else:
            stage.plot(offset, label_offset=label_offset, ax=ax)

        if label_offset is not None:
            ax.text(-0.1, 0, -0.2, r"$\Sigma_0$", size=14)
        label_offset = None  # show the labels only for the first frame
    return ax


def ax_config(
    ax: Axes3D,
    elev: float = 15,
    azim: float = -60,
    xlim: tuple[float, float] = (1, 5),
    ylim: tuple[float, float] = (-1.5, 1.5),
    zlim: tuple[float, float] = None,
) -> Axes3D:
    """Configure axes."""
    if xlim is not None:
        ax.set_xlim(xlim)

    if ylim is not None:
        ax.set_ylim(ylim)

    if zlim is not None:
        ax.set_zlim(zlim)

    ax.set_aspect("equal")
    ax.set_axis_off()

    ax.view_init(elev=elev, azim=azim)

    return ax


def euler_xyz_around_fixed_frame(I, rx, ry, rz):
    ax = ax_config(show_seq_rot([I, (rx, 1.4), (ry @ rx, 2.8), (rz @ ry @ rx, 4.1)]))

    ax.figure.savefig(
        "out/euler_xyz_around_fixed_frame.pgf",
        backend="pgf",
        transparent=True,
        bbox_inches=ax.figure.bbox_inches.from_bounds(1.15, 2.55, 5.5, 3.3),
    )


def euler_zyx_around_current_frame(I, rx, ry, rz):
    ax = ax_config(show_seq_rot([I, (rz, 2.4), (rz @ ry, 3.7), (rz @ ry @ rx, 4.1)]))

    ax.figure.savefig(
        "out/euler_zyz_around_current_frame.pgf",
        backend="pgf",
        transparent=True,
        bbox_inches=ax.figure.bbox_inches.from_bounds(1.15, 2.55, 5.5, 3.3),
    )


if __name__ == "__main__":
    I = RotationMatrix()
    rx = RotationMatrix.x(np.pi / 2)
    ry = RotationMatrix.y(np.pi / 2)
    rz = RotationMatrix.z(np.pi / 2)

    args = get_parser().parse_args()

    if args.fixed_frame:
        euler_xyz_around_fixed_frame(I, rx, ry, rz)
    else:
        euler_zyx_around_current_frame(I, rx, ry, rz)
