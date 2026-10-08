import numpy as np

array = np.random.randint(1, 100, 9)
print("Original Array:\n", array)

print("\nSquare Root:\n", np.sqrt(array))
print("\nDimensions of array:", array.ndim)

new_array = array.reshape(3, 3)
print("\nReshaped 3x3 Array:\n", new_array)
print("Dimensions of new_array:", new_array.ndim)

print("\nFlattened Array (ravel):\n", new_array.ravel())

newm = new_array.reshape(3, 3)
print("\nSlice newm[2, 1:3]:\n", newm[2, 1:3])
print("\nSlice newm[1:2, 1:3]:\n", newm[1:2, 1:3])
print("\nSlice new_array[0:3, 0:0]:\n", new_array[0:3, 0:0])
print("\nSlice new_array[0:2, 0:1]:\n", new_array[0:2, 0:1])
print("\nSlice new_array[0:3, 0:1]:\n", new_array[0:3, 0:1])
print("\nSlice new_array[1:3]:\n", new_array[1:3])