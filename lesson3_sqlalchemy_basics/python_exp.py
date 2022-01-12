import functools
def make_divisibility_test(n):
    def divisible_by_n(m):
        return m % n == 0
    return divisible_by_n

div_by_3 = make_divisibility_test(3)
print(tuple(filter(div_by_3, range(10))))

result = make_divisibility_test(5) (7)
print(result)

def print_args(function):
    @functools.wraps(function)
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        print(function(*args, **kwargs))
        return function(*args, **kwargs)
    return wrapper

def compute(x, y, z=1):
    return (x + y) * z

result1 = compute(3, 5, z=2)
print(result1)
compute_log = print_args(compute)
compute_log(3, 5, z=2)

@print_args
def compute2(x, y, z=1):
    """I am the compute function."""
    return (x + y) * z

compute2(4, 5, z=3)
print(compute2.__doc__)