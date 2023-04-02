# Optimization
from scipy.optimize import minimize

def f(x):
    return x**2

result = minimize(f, x0=2)
print(result)

