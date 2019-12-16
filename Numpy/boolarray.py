# Create a 3×3 numpy array of all True’s

import numpy as np

array = np.full((3, 3), True, dtype=bool)

# alternative method
# array = np.ones((3, 3), dtype=bool)
print(array)