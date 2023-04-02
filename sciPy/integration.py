#Integration
from scipy.integrate import quad

def f(x):
    return x**2

result, error = quad(f, 0, 1)
print(result)
