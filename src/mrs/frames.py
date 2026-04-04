from __future__ import annotations


import numpy as np


from mrs.vizu import FramePainterMixin

import matplotlib.pyplot as plt
import math


class Frame:
    """A class to represent a position with x, y, z coordinates and angles"""

    def __init__(self, x=0, y=0, z=0, angletox=0, angletoy=0, angletoz=0):
        self.x = x
        self.y = y
        self.z = z
        self.angletox = angletox % 360
        self.angletoy = angletoy % 360
        self.angletoz = angletoz % 360

    def combinematrixes(self):
        """Convert angles to rotation matrix"""
        rad_x = math.radians(self.angletox)
        rad_y = math.radians(self.angletoy)
        rad_z = math.radians(self.angletoz)

        Rx = RotationMatrix.x(rad_x)

        Ry = RotationMatrix.y(rad_y)

        Rz = RotationMatrix.z(rad_z)

        return Rz @ Ry @ Rx

    def plot(self, ax=None, scale=1.0):
        """Visualize the frame in 3D"""
        if ax is None:
            fig = plt.figure(figsize=(10, 8))
            ax = fig.add_subplot(1, 1, 1, projection="3d")

        R = self.get_rotation_matrix()
        x_axis = R[:, 0] * scale
        y_axis = R[:, 1] * scale
        z_axis = R[:, 2] * scale
        pos = np.array([self.x, self.y, self.z])

        # drawign axes with arrows
        ax.quiver(
            pos[0],
            pos[1],
            pos[2],
            x_axis[0],
            x_axis[1],
            x_axis[2],
            color="red",
            arrow_length_ratio=0.1,
            linewidth=2,
        )
        ax.quiver(
            pos[0],
            pos[1],
            pos[2],
            y_axis[0],
            y_axis[1],
            y_axis[2],
            color="green",
            arrow_length_ratio=0.1,
            linewidth=2,
        )
        ax.quiver(
            pos[0],
            pos[1],
            pos[2],
            z_axis[0],
            z_axis[1],
            z_axis[2],
            color="blue",
            arrow_length_ratio=0.1,
            linewidth=2,
        )

        # name of arrows
        ax.text(
            pos[0] + x_axis[0] * 1.1,
            pos[1] + x_axis[1] * 1.1,
            pos[2] + x_axis[2] * 1.1,
            "X",
            color="red",
            fontsize=12,
            fontweight="bold",
        )
        ax.text(
            pos[0] + y_axis[0] * 1.1,
            pos[1] + y_axis[1] * 1.1,
            pos[2] + y_axis[2] * 1.1,
            "Y",
            color="green",
            fontsize=12,
            fontweight="bold",
        )
        ax.text(
            pos[0] + z_axis[0] * 1.1,
            pos[1] + z_axis[1] * 1.1,
            pos[2] + z_axis[2] * 1.1,
            "Z",
            color="blue",
            fontsize=12,
            fontweight="bold",
        )

        # origin
        if self.x == 0 and self.y == 0 and self.z == 0:
            ax.scatter([0], [0], [0], color="black", s=50, marker="o")

        ax.set_xlabel("X axis")
        ax.set_ylabel("Y axis")
        ax.set_zlabel("Z axis ")

        return ax


class RotationMatrix(FramePainterMixin):
    def __init__(self, R=None) -> None:
        self.R = np.eye(3) if R is None else R

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
