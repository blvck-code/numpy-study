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
print('Total size ==>>', a.size)  # total number of elements in array
print('Total size ==>>', b.size)  # total number of elements in array


# How to create a basic array
# This section covers np.zeros(), np.ones(), np.empty(), np.arange(), np.linspace()

c = np.zeros(2) # array filled with zeros
d = np.ones(2) # array filled with ones
e = np.empty(2)

print(c)
print(d)
print(3)

f = np.arange(4) # create array with a range of elements
print(f)


g = np.arange(2, 9, 2) #even an array that contains a range of evenly spaced intervals.
# To do this, you will specify the first number, last number, and the step size.
print(g)



