import time

def timer(func):
    def f (*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("Time taken: ", end - start)
        return res
    
    return f

def ntimes(n):
    def inner(f):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                print(f"running {f.__name__}")
                res = f(*args, **kwargs)
            return res
        return wrapper
    return inner


@timer
def add(x , y):
    return x + y

@ntimes(4)
def sub(x, y):
    return x - y

print("res:", add(2,5))
print("res:", sub(10, 5))
