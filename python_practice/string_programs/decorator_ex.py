def log_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[LOG] Function {func.__name__} finished execution")
        return result
    return wrapper
@log_decorator
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")
