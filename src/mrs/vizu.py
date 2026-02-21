from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
from mpl_toolkits.mplot3d.axes3d import Axes3D


class FramePainterMixin:
    def plot(
        self,
        r: Optional[list | np.ndarray] = None,
        color: Optional[str | dict[str, str]] = None,
        label_offset: Optional[float] = None,
        ax: Optional[Axes3D] = None,
        figsize: tuple[int, int] = (8, 8),
    ) -> Axes3D:
        if ax is None:
            fig = plt.figure(figsize=figsize)
            ax = fig.add_subplot(111, projection="3d")

        if color is None:
            colors = {"x": "r", "y": "g", "z": "b"}
        elif isinstance(color, str):
            colors = {key: color for key in list("xyz")}
        else:
            colors = color

        r = np.zeros(3) if r is None else np.array(r)

        x, y, z = r + self.R.T
        ax.plot(*[(s, e) for s, e in zip(r, x)], color=colors["x"])
        ax.plot(*[(s, e) for s, e in zip(r, y)], color=colors["y"])
        ax.plot(*[(s, e) for s, e in zip(r, z)], color=colors["z"])

        if label_offset is not None:
            x_label, y_label, z_label = r + label_offset * self.R.T
            ax.text(*x_label, "$x$", size=12)
            ax.text(*y_label, "$y$", size=12)
            ax.text(*z_label, "$z$", size=12)

        Ry = np.array([[0, 0, 1], [0, 1, 0], [-1, 0, 0]])
        Rx = np.array([[1, 0, 0], [0, 0, 1], [0, -1, 0]])
        self._pyramid(ax, r + self.R @ np.array([1, 0, 0]), self.R @ Ry, color="r")
        self._pyramid(ax, r + self.R @ np.array([0, 1, 0]), self.R @ Rx, color="g")
        self._pyramid(ax, r + self.R @ np.array([0, 0, 1]), self.R, color="b")

        return ax

    @staticmethod
    def _pyramid(
        ax,
        r=None,
        R=None,
        scale=0.03,
        base_height_ratio=8 / 3,
        **kwargs,
    ):
        position = np.array([0, 0, 0]) if r is None else np.array(r)
        rotation = np.eye(3) if R is None else R

        apex0 = np.array([0.0, 0.0, scale * base_height_ratio])
        base0 = scale * np.array(
            [
                [-0.5, -0.5, 0.0],
                [0.5, -0.5, 0.0],
                [0.5, 0.5, 0.0],
                [-0.5, 0.5, 0.0],
            ]
        )

        vertices = position + np.vstack((base0, apex0)) @ rotation.T
        apex, base = vertices[4], vertices[:4]
        faces = [
            base,
            [base[0], base[1], apex],
            [base[1], base[2], apex],
            [base[2], base[3], apex],
            [base[3], base[0], apex],
        ]
        poly = Poly3DCollection(faces, **kwargs)
        ax.add_collection3d(poly)
        return ax
