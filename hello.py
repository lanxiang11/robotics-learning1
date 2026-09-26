import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("矩阵 A：")
print(A)

print("矩阵 B：")
print(B)

print("A + B：")
print(A + B)

print("A - B：")
print(A - B)

print("矩阵元素乘法：")
print(A * B)

print("矩阵乘法：")
print(A @ B)