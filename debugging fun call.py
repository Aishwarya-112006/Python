#create a decorator that prints the name of the function being called and its arguments every time a func is called

def debug(func):
    def wrapper(*args, **kwargs):
        args_value=', '.join(str(arg) for arg in args)#gives iterable in string form
        kwargs_value=','.join(f"{k}={v}" for k, v in kwargs.items())

        print(f"Calling function: {func.__name__}")
        print(f"Arguments: {args_value}, Keyword Arguments: {kwargs_value}")

        return func(*args, **kwargs)
    return wrapper

@debug
def add(a,b):
    return a+b
add(10,20)
@debug
def greet(name, msg="hi"):
    print(f"{msg},{name}!")

greet("sid", msg="hello")