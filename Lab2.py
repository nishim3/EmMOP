import numpy as np
import matplotlib.pyplot as plt

I = 1  # Current in amperes
Z = 20  # Depth in meters
x = np.arange(1, 1001, 10)  # 1000 meter interval
x0 = 500  # Position of the wire

# Calculate distance from wire to each point
r = np.sqrt(Z**2 + (x - x0)**2)

# Calculate magnetic field components
Hx = np.zeros_like(x)
Hz = np.zeros_like(x)

# Find indices where r is not zero to avoid division by zero
nonzero_indices = r != 0

# Hx formula
Hx[nonzero_indices] = I / (2 * np.pi * r[nonzero_indices]) * Z

# Hz formula
Hz[nonzero_indices] = I / (2 * np.pi * r[nonzero_indices]) * (x[nonzero_indices] - x0)

# Plot Hx vs x
plt.figure()
plt.plot(x, Hx, 'b-', linewidth=2)
plt.xlabel('Distance (m)')
plt.ylabel('Hx (A/m)')
plt.title('Magnetic Field Hx vs Distance x')
plt.grid(True)

# Plot Hz vs x
plt.figure()
plt.plot(x, Hz, 'r-', linewidth=2)
plt.xlabel('Distance (m)')
plt.ylabel('Hz (A/m)')
plt.title('Magnetic Field Hz vs Distance x')
plt.grid(True)

plt.show()
