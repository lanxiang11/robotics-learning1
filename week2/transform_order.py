import numpy as np

def rotation_matrix(angle_degrees):
    angle = np.deg2rad(angle_degrees)
    return np.array([
        [np.cos(angle), -np.sin(angle)],
        [np.sin(angle),  np.cos(angle)],
    ])


point = np.array([1.0, 0.0])
translation = np.array([2.0, 0.0])
R = rotation_matrix(90)

# 先旋转，再平移
result_a = R @ point + translation

# 先平移，再旋转
result_b = R @ (point + translation)

print("先旋转，再平移：", np.round(result_a, 6))
print("先平移，再旋转：", np.round(result_b, 6))