import time
from functools import wraps

def ttl_cache(seconds: int):
    """A decorator that caches the result of a function call for a specified number of seconds."""
    def decorator(func):
        cache = {}
        cache_time = {}

        @wraps(func)
        def wrapper(*args, **kwargs):
            current_time = time.time()
            if args in cache and (current_time - cache_time[args]) < seconds:
                return cache[args]
            result = func(*args, **kwargs)
            cache[args] = result
            cache_time[args] = current_time
            return result

        return wrapper
    return decorator
