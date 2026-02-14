from __future__ import annotations

import os
from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.axes3d import Axes3D


class Frame: ...


class RotationMatrix:
    def __init__(self, R=None) -> None:
        self.R = np.eye(3) if R is None else R

    def plot(
        self,
        r: Optional[list | np.ndarray] = None,
        color: Optional[str | dict[str, str]] = None,
        label_offset: float = 1.1,
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

        x_label, y_label, z_label = r + label_offset * self.R.T
        ax.text(*x_label, "$x$", color=colors["x"])
        ax.text(*y_label, "$y$", color=colors["y"])
        ax.text(*z_label, "$z$", color=colors["z"])

        return ax

    def __matmul__(self, other: RotationMatrix) -> RotationMatrix:
        return RotationMatrix(self.R @ other.R)

    @staticmethod
    def x(angle: float = 0) -> RotationMatrix:
        return RotationMatrix(
            np.array(
                [
                    [1, 0, 0],
                    [0, np.cos(angle), -np.sin(angle)],
                    [0, np.sin(angle), np.cos(angle)],
                ]
            )
        )

    @staticmethod
    def y(angle: float = 0) -> RotationMatrix:
        return RotationMatrix(
            np.array(
                [
                    [np.cos(angle), 0, np.sin(angle)],
                    [0, 1, 0],
                    [-np.sin(angle), 0, np.cos(angle)],
                ]
            )
        )

    @staticmethod
    def z(angle: float = 0) -> RotationMatrix:
        return RotationMatrix(
            np.array(
                [
                    [np.cos(angle), -np.sin(angle), 0],
                    [np.sin(angle), -np.cos(angle), 0],
                    [0, 0, 1],
                ]
            )
        )
