import functools
import time
import collections
from typing import Callable, Any

def compose(*functions: Callable) -> Callable:
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions, lambda x: x)

def memoize_with_expiry(seconds: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        cache = {}
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            key = (args, frozenset(kwargs.items()))
            now = time.time()
            if key in cache:
                result, timestamp = cache[key]
                if now - timestamp < seconds:
                    return result
            result = func(*args, **kwargs)
            cache[key] = (result, now)
            return result
        return wrapper
    return decorator

def deep_flatten(items: Any) -> list:
    result = []
    for item in items:
        if isinstance(item, (list, tuple)):
            result.extend(deep_flatten(item))
        else:
            result.append(item)
    return result

def flip_dict(d: dict) -> dict:
    return {v: k for k, v in d.items()}

def throttle(limit: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        calls = collections.deque()
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            now = time.time()
            while calls and calls[0] < now - 1:
                calls.popleft()
            if len(calls) < limit:
                calls.append(now)
                return func(*args, **kwargs)
            raise RuntimeError("rate limit exceeded")
        return wrapper
    return decorator