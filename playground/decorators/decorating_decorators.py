import functools
import time


def hello():
    return "Hello world"


def decorate(func):
    def wrap(*arg, **kwargs):
        print("I am a before decorator")
        print(func(*arg, **kwargs))
        print("I am after decorator")

    return wrap


def performance_counter(f):
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        func = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"the function {f.__name__} took {end - start} in")
        return func

    return wrapper


# @performance_counter
@decorate
def hello(name):
    return f"Hello {name}"


@performance_counter
def add(x, y):
    return x + y


# hello = decorate(hello)

print(hello("Banke"))
print(add(2, 3))
# print(performance_counter("Banke"))
