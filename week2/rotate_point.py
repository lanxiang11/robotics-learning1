import numpy as np

def rotation_matrix(angle_degrees):
    """根据角度（单位：度）生成二维旋转矩阵。"""
    angle_radians = np.deg2rad(angle_degrees)

    return np.array([
        [np.cos(angle_radians), -np.sin(angle_radians)],
        [np.sin(angle_radians),  np.cos(angle_radians)],
    ])


point = np.array([1.0, 0.0])

for angle in [0, 90, 180, 270]:
    rotated = rotation_matrix(angle) @ point
    print(f"旋转 {angle}°：{np.round(rotated, 6)}")

