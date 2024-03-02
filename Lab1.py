# Program to compute the magnetic field inside a large loop transmitter

import numpy as np
import matplotlib.pyplot as plt

# Define lengths on x and y axis
a = 100
b = 100

# Coordinates of the origin
p = 0
q = 0

# Define current given to the loop
I = 1

# Calculate magnetic field for each integer point in the 0,0 to 100,100 space (excluding 0,0 and 100,100)
x_values = np.arange(1, 100, 2)
y_values = np.arange(1, 100, 2)

magnetic_field_values = []

for x in x_values:
    for y in y_values:
        # Calculate distances from the variable point to the vertices of the loop
        r1 = np.sqrt((x - p)**2 + (y - q)**2)
        r2 = np.sqrt((a - x)**2 + (q - y)**2)
        r3 = np.sqrt((a - x)**2 + (b - y)**2)
        r4 = np.sqrt((p - x)**2 + (b - y)**2)

        # Calculate areas of the four sectors
        A1 = (x - p) * (y - q)
        A2 = (a - x) * (y - q)
        A3 = (a - x) * (b - y)
        A4 = (x - p) * (b - y)

        # Calculate magnetic field H
        mu_0 = 4 * np.pi * 1e-7  # Magnetic constant (permeability of free space)
        H = (I / (4 * np.pi)) * (r1 / A1 + r2 / A2 + r3 / A3 + r4 / A4)

        magnetic_field_values.append(H)

# Reshape magnetic_field_values to match the shape of the grid
magnetic_field_grid = np.array(magnetic_field_values).reshape(len(x_values), len(y_values))

# Plot the contour plot of the magnetic field
plt.figure(figsize=(10, 8))
contour = plt.contour(x_values, y_values, magnetic_field_grid, levels=500, cmap='viridis')
plt.colorbar(contour, label='Magnetic Field (A/m)')
plt.title('Contour Plot of Magnetic Field Distribution')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.show()
