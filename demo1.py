import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# 二连杆长度
L1 = 1.0
L2 = 0.8

# 创建画布
fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.set_xlim(-(L1 + L2), L1 + L2)
ax.set_ylim(-(L1 + L2), L1 + L2)
ax.grid(True)

# 机械臂线条和关节点
arm_line, = ax.plot([], [], "o-", lw=4, color="blue")
trace_line, = ax.plot([], [], "--", color="red", alpha=0.6)

trace_x = []
trace_y = []

def inverse_kinematics(x, y):
    """二连杆逆运动学，返回两个关节角"""
    cos_theta2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    cos_theta2 = np.clip(cos_theta2, -1, 1)

    theta2 = np.arccos(cos_theta2)

    theta1 = np.arctan2(y, x) - np.arctan2(
        L2 * np.sin(theta2),
        L1 + L2 * np.cos(theta2)
    )

    return theta1, theta2

def update(frame):
    # 目标点：圆周运动
    t = frame * 0.05
    x = 1.0 + 0.35 * np.cos(t)
    y = 0.35 + 0.35 * np.sin(t)

    theta1, theta2 = inverse_kinematics(x, y)

    # 正运动学
    joint1_x = L1 * np.cos(theta1)
    joint1_y = L1 * np.sin(theta1)

    end_x = joint1_x + L2 * np.cos(theta1 + theta2)
    end_y = joint1_y + L2 * np.sin(theta1 + theta2)

    arm_line.set_data(
        [0, joint1_x, end_x],
        [0, joint1_y, end_y]
    )

    trace_x.append(end_x)
    trace_y.append(end_y)
    trace_line.set_data(trace_x, trace_y)

    return arm_line, trace_line

animation = FuncAnimation(
    fig,
    update,
    frames=500,
    interval=30,
    blit=True
)

plt.title("二连杆机械臂运动仿真")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()