import time


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        finish = time.perf_counter() - start
        print(f'Executed {func.__name__} in {finish:0.2f} seconds')
        return result
    return wrapper
