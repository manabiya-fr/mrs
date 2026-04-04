from __future__ import annotations


import numpy as np


from mrs.vizu import FramePainterMixin

import matplotlib.pyplot as plt
import math


class Frame:
    """A class to link the rotation matrix and position vector to visualisation"""

    def __init__(self, r, R):
        self.r = r
        self.R = R

    def plot(self):
        self.R.plot(self.r)


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
