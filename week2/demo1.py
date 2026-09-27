import numpy as np

# 从原点指向 (3, 4) 的向量
v = np.array([3.0, 4.0])

print("向量 v：", v)
print("x 分量：", v[0])
print("y 分量：", v[1])
print("向量长度：", np.linalg.norm(v))

start = np.array([1.0, 2.0])
end = np.array([4.0, 6.0])

displacement = end - start
distance = np.linalg.norm(displacement)

print("从起点到终点的位移：", displacement)
print("两点间距离：", distance)