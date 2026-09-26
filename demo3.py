import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 10, 1000)

x = t
y = 0.5 * t

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Point Motion")
plt.grid(True)
plt.axis("equal")
plt.show()