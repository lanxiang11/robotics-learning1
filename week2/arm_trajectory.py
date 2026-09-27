import numpy as np
import matplotlib.pyplot as plt

L1 = 1.0
L2 = 0.8

theta1_values = np.linspace(0, 180, 100)
theta2_degrees = 45

end_x = []
end_y = []

for theta1_degrees in theta1_values:
    theta1 = np.deg2rad(theta1_degrees)
    theta2 = np.deg2rad(theta2_degrees)

    x = L1 * np.cos(theta1) + L2 * np.cos(theta1 + theta2)
    y = L1 * np.sin(theta1) + L2 * np.sin(theta1 + theta2)

    end_x.append(x)
    end_y.append(y)

plt.plot(end_x, end_y, label="End-effector path")
plt.scatter(end_x[0], end_y[0], color="green", label="Start")
plt.scatter(end_x[-1], end_y[-1], color="red", label="End")

plt.xlabel("X")
plt.ylabel("Y")
plt.title("Two-Link Arm End-Effector Path")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.savefig("week2/arm_trajectory.png", dpi=150)
plt.show()