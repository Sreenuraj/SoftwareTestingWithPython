import functools


def my_decorator(func):
    @functools.wraps(func)
    def functions_that_run_func():
        print('In decorator')
        func()
        print('After the decorator')
    return functions_that_run_func


@my_decorator
def my_function():
    print('in my function')


# my_function()

def decorator_with_arguments(num):
    def my_decorator(func):
        @functools.wraps(func)
        def functions_that_run_func(*args, **kwargs):
            print('In decorator')
            if num == 56:
                print("not running")
            else:
                func(*args, **kwargs)
            print('After the decorator')
        return functions_that_run_func
    return my_decorator


@decorator_with_arguments(56)
def my_fuction(x, y):
    print(x + y)


my_fuction(10, 5)
