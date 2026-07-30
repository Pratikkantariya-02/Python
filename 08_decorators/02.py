def debug(func):
    def wrapper(*args,**kwargs):
        # args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k} = {v}" for k,v in kwargs.items())
        print(f"calling: {func.__name__} with args {kwargs_value}")
        return func(*args,**kwargs)

    return wrapper

@debug
def greet(name, greeting = "hello"):
    print(f"{greeting}, {name}")

greet("chai", greeting = "hello")