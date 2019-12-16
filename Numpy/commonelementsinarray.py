# Get the common items between two arrays
import numpy as np

a = np.array([1, 2, 3, 2, 3, 4, 3, 4, 5, 6])
print("First array: {}".format(a))

b = np.array([7, 2, 10, 2, 7, 4, 9, 4, 9, 8])
print("First array: {}".format(b))

c = np.intersect1d(a, b)
print("The intersection of both arrays is: {}".format(c))

# If you want to remove the common elements you might do as follows
c = np.setdiff1d(a, b)
print("The result of removing common elements from first array is: "
      "{}".format(c))

# If you want to find out the index of the common elements in two arrays
index = np.where(a == b)
print("The positions of matchess are {}".format(index))