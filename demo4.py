import numpy as np
import matplotlib.pyplot as plt

# 两根连杆长度
l1 = 1.0
l2 = 0.8

# 两个关节角，单位：弧度
theta1 = np.deg2rad(30)
theta2 = np.deg2rad(45)

# 第一个关节位置
x0 = 0
y0 = 0

# 第二个关节位置
x1 = l1 * np.cos(theta1)
y1 = l1 * np.sin(theta1)

# 末端位置
x2 = x1 + l2 * np.cos(theta1 + theta2)
y2 = y1 + l2 * np.sin(theta1 + theta2)

print("末端位置：")
print("x =", x2)
print("y =", y2)

# 绘制机械臂
plt.plot([x0, x1, x2], [y0, y1, y2], "o-", linewidth=3)
plt.scatter(x2, y2, s=100, label="end-effector")

plt.xlim(-2, 2)
plt.ylim(-2, 2)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Two Link Robot Arm")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()