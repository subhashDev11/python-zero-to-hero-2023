# Decorators
import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start} seconds to execute")
        return result
    return wrapper

@time_it
def some_function():
    time.sleep(1)

some_function() # Output: some_function took 1.000166893005371 seconds to execute

def authenticate(func):
    def wrapper(*args, **kwargs):
        # check if user is authenticated
        if user_authenticated():
            return func(*args, **kwargs)
        else:
            raise Exception("User not authenticated")
    return wrapper

@authenticate
def some_function():
    pass

def user_authenticated():
    return True

some_function() # Output: No exception raised
