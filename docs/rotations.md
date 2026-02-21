# Sequences of rotations

A minimal parameterization of orientation can be obtained by using a set of three angles
$\{\alpha, \beta, \gamma\}$ together with an admissible composition sequence. A sequence
of rotations is considered to be "admissible" if no two successive rotations are made
around parallel axes. For example, Figure 1 depicts three successive rotations around
the $x \to y \to z$ axes of a fixed frame $\Sigma_0$ (all at angles $\pi/2$)

<figure markdown="span">
  ![Image title](figures/euler_xyz_around_fixed_frame.svg){ width="800" }
  <figcaption>Figure 1: Example of XYZ rotations around a fixed frame.</figcaption>  
</figure>

+ $R_x(\pi/2)$
+ $R_y(\pi/2)R_x(\pi/2)$
+ $R_z(\pi/2)R_y(\pi/2)R_x(\pi/2)$


<figure markdown="span">
  ![Image title](figures/euler_zyz_around_current_frame.svg){ width="800" }
  <figcaption>Figure 1: Example of ZYX rotations around the current frame.</figcaption>  
</figure>

+ $R_z(\pi/2)$
+ $R_z(\pi/2)R_y(\pi/2)$
+ $R_z(\pi/2)R_y(\pi/2)R_x(\pi/2)$



