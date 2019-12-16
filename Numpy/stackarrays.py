# Stack two arrays vertically
import numpy as np

a = np.arange(10).reshape(2, -1)
print("First array")
print(a)

b = np.arange(11, 21).reshape(2, -1)
print("Second array")
print(b)

c = np.vstack([a, b])
print("The result after vertical stacking is")
print(c)

# The above result could also be obtained using concatenate
# c = np.concatenate([a, b], axis=0)

# Also to stack the arrays horizontally, we could either use
# hstack or use axis=1 in concatenate
# c = np.vstack([a, b])
# c = np.concatenate([a, b], axis=1)