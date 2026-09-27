import numpy as np
import matplotlib.pyplot as plt

point = np.array([1.0, 0.0])
angles = np.linspace(0, 360, 100)

x_values = []
y_values = []

for angle_degrees in angles:
    angle = np.deg2rad(angle_degrees)

    R = np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle),  np.cos(angle)],
    ])

    rotated = R @ point
    x_values.append(rotated[0])
    y_values.append(rotated[1])

plt.plot(x_values, y_values, label="Rotated point path")
plt.scatter([0], [0], color="black", label="Origin")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Rotation Around the Origin")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.savefig("week2/rotation_path.png", dpi=150)
plt.show()