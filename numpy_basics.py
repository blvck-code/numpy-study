import numpy as np

a = np.array([1, 2, 3], dtype='int16')
print("Array:", a)
print("Mean:", np.mean(a))
print("Sum:", np.sum(a))

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
print(b)
print('Dimension ==>>', b.ndim)
print('Shape ==>>', b.shape)
print('Type ==>>', b.dtype)
print('Type ==>>', a.dtype)
print('Size ==>>', a.itemsize)
print('Total size ==>>', a.size)