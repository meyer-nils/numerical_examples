# Numerical examples
Application of several numerical algorithms and tools in Python to engineering problems.

## One-dimensional heat equation
Transient heat equation with fixed temperature at one end. 

Solved with: 
- scikit-fem (second order elements and Crank-Nicolson time integration)
- nutils_iga (second degree spline elements and Crank-Nicolson time integration)
- fenicsx (first order elements and implicit time integration)
- tensorflow (PINN with five fully connected hidden layers)
- pytorch (PINN with five fully connected hidden layers)

![heat transfer](heat_transfer_1d.png)


## Two-dimensional plate hole example
Elastic problem of a simple plate with a hole.

Solved with: 
- scikit-fem (first order elements)
- nutils (second order standard elements)
- nutils_iga (second order spline elements)
- fenicsx (first order elements)
- tensorflow (PINN with five fully connected hidden layers)
- pytorch (PINN with five fully connected hidden layers)

![plate hole](plate_hole_2d.png)