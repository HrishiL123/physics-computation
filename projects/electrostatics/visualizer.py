import numpy as np
import matplotlib.pyplot as plt
from projects.electrostatics.field import electric_field
from projects.electrostatics.potential import total_potential

# List of charges: (q in C, [x, y] position)
charges = [
    (1e-9, [0, 0]),    # positive charge at origin
    (-1e-9, [1, 0])    # negative charge at x=1 m
]
# 2D grid from -1 to 2 meters in x and y, 50 points each
x = np.linspace(-1, 2, 50)
y = np.linspace(-1, 1, 50)
X, Y = np.meshgrid(x, y)

# Flatten the grid for easy computation
points = np.array([ [xi, yi] for xi, yi in zip(X.flatten(), Y.flatten()) ])

# Compute total potentials and reshape back to grid
V = np.array(total_potential(charges, points)).reshape(X.shape)

# Compute total electric field vectors
E_vectors = electric_field(charges, points)
Ex = np.array([vec[0] for vec in E_vectors]).reshape(X.shape)
Ey = np.array([vec[1] for vec in E_vectors]).reshape(X.shape)

plt.figure(figsize=(8, 4))

# 1️⃣ Electric field vectors
plt.quiver(X, Y, Ex, Ey, color='blue', alpha=0.5)
plt.title("Electric Field Vectors")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.axis('equal')
plt.show()

# 2️⃣ Equipotential lines
plt.figure(figsize=(8, 4))
plt.contour(X, Y, V, levels=20, cmap='inferno')
plt.title("Equipotential Lines")
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.axis('equal')
plt.colorbar(label='Potential (V)')
plt.show()
