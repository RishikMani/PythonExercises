import numpy as np

a = np.array([1, 2, 3])
print(a)

# np.r_ Translates slice objects to concatenation along the first axis.
# It returns a concatenated ndarray or matrix.
b = np.r_[np.repeat(a, 3), np.tile(a, 3)]
print(b)