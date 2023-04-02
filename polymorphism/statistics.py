#Statistics
import numpy as np
from scipy import stats

data = np.array([1, 2, 3, 4, 5])

mean = stats.gmean(data)
std = stats.gstd(data)
var = stats.variation(data)

print("Mean: ", mean)
print("Standard deviation: ", std)
print("Coefficient of variation: ", var)
