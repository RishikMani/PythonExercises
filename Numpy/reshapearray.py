# Convert a 1D array to a 2D array with 2 rows
import numpy as np

a = np.arange(10)
print("The input array is {}".format(a))

# Setting to -1 automatically decides the number of columns
a = a.reshape(2, -1)
print("Reshaping the array outputs:")
print(a)