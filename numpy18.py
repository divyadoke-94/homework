import numpy as np

arr1 = np.array([1,2,3,4,5])
arr2 = np.array([1,2,3] ,[4,5,6])

print("1D Array:",arr1)
print("2D Array:\n",arr2)

zeros = np.zeros((2,3))
ones = np.ones((3,3))
identity = np.eye(4)

print("zeros:\n",zeros)
print("ones:\n",ones)
print("identity matrix:\n",identity)

ararnge_arr = np.arrange(0,10,2)
linspace_arr = np.linspace(0,1,5)

rand_arr = np.random.rand(2,3)
print("random array:\n",rand_arr)

matrix = np.arrange(1,13).reshape(2,6)
print("matrix:\n",matrix)
print("Transpose:\n",matrix.T)

arr = np.array([10,20,30,40])
print("original Array:",arr)
print("Array + 5:", arr + 5)
print("array squared:", arr ** 2)

print("sum:", np.sum(arr))
print("Mean:",np.mean(arr))
print("standard Deviation:",np.std(arr))

