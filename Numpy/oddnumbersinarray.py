# Extract all odd numbers from an array

import numpy as np

array = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print("The odd numbers in the array are {0}".format(array[array % 2 == 1]))

# Replace all odd numbers in arr with -1
array[array % 2 == 1] = -1
print("The array after replacing all odd numbers with -1 is: "
      "{}".format(array))

out = np.where(array[array % 2 == 1], -1, array)
print("Replacing the odd numbers from orginal array without affecting the "
      "original array is {}".format(out))
