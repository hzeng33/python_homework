# Task 1: Writing and Testing a Decorator
import logging

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))

def logger_decorator(func):
    def wrapper(*args, **kwargs):
        if args:
            pos_params = list(args)
        else:
            pos_params = "none"
        
        if kwargs:
            kw_params = dict(kwargs)
        else:
            kw_params = "none"
        
        result = func(*args, **kwargs)
        
        log_message = f"function: {func.__name__}\n positional parameters: {pos_params}\n keyword parameters: {kw_params}\n return: {result}\n"
        
        logger.log(logging.INFO, log_message)
        return result
    return wrapper

@logger_decorator
def hello_world():
    print("Hello, world!")
    return None

@logger_decorator
def take_args(*args):
    print(f"Received {len(args)} positional arguments: {args}")
    return True

@logger_decorator
def take_kwargs(**kwargs):
    print(f"Received keyword arguments: {kwargs}")
    return logger_decorator

hello_world()
take_args(1, 2, 3, "Hello", 4.5)
take_kwargs(name="May", age=28, city="New York")