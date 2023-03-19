# Numerical examples
Application of several numerical algorithms and tools in Python to engineering problems.

## One-dimensional heat equation
Transient heat equation with fixed temperature at one end. 

Solved with: 
- scikit-fem (second order elements and Crank-Nicolson time integration)
- Nutils (IGA with second degree spline elements and Crank-Nicolson time integration)
- FEniCSx (first order elements and implicit time integration)
- TensorFlow (PINN with five fully connected hidden layers)
- PyTorch (PINN with five fully connected hidden layers)

## Two-dimensional plate hole example
Elastic problem of a simple plate with a hole.

Solved with: 
- scikit-fem (first order elements)
- Nutils (second order standard elements)
- Nutils (IGA with second order spline elements)
- FEniCSx (first order elements)
- TensorFlow (PINN with five fully connected hidden layers)
- PyTorch (PINN with five fully connected hidden layers)