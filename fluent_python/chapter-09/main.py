import functools
from typing import Any
import time


b = 6 

def f1(a):
    # global keyword
    global b
    print(a)
    print(b)
    
    b = 9

f1(20)
print(b) 

class averager:
    def __init__(self) -> None:
        self.series = []
        
    def __call__(self, new_value) -> Any:
        self.series.append(new_value)
        total = sum(self.series)
        return total / len(self.series)
        
avg = averager()
avg(11)
avg(23)
print(avg(10))

def make_average():
    count = 0
    total = 0
    
    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager
# -----------------------------------------------------

def clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        name = func.__name__
        args_list = [repr(arg) for arg in args]
        args_list.extend(f"{k}={v!r}" for k , v in kwargs.items())
        args_str = ", ".join(args_list)
        print(f"[{elapsed:0.8f}s] {name}({args_str}) -> {result!r}")
        return result
    return clocked

@clock
def snooze(seconds):
    time.sleep(seconds)

@clock
def factorial(n):
    return 1 if n <= 1 else  n * factorial(n-1)

print('*' * 40, 'calling snooze(.123)')
snooze(.123)
print('*' * 40, 'calling factorial(6)')
print('6! =', factorial(6))
# ---------------------------------

# @functools.cache
# @functools.lru_cache
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + (n - 1)

print(fibonacci(5))