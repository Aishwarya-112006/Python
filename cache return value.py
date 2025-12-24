#implement ation of a simple cache decorator that caches the return value of a function based on its arguments, so when its called with the same argument .the cached value is returned instead of rexecuting the function again
import time
def cache(fun):
    
    cache_value={}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
            cache_value[args]=result
        result=fun(*args)
        return result
    return wrapper
@cache
def long(a,b):
    time.sleep(5)
    return a+b
long(20,56)