def decorator(func):
    def wrapper():
        print('Something before func is called')
        func()
        print('Something after func is called')
    return wrapper

@decorator
def say_hello():
    print('hello')

say_hello()

def say_hello2():
    print('Hello22')

say_hello22 = decorator(say_hello2)
print(say_hello22)

say_hello22()

def new_decorator(func):
    def wrapper(*args, **kwargs):
        print('SOME THING BEFORE')
        result = func(*args, **kwargs)
        print('SOME THING AFTER')
        return result
    return wrapper

@new_decorator
def hello_name(name):
    print(f'Hello, {name}')



hello_name('Hillel')

def validate(*args, **kwargs):
    for arg in args:
        print(arg)
        for ar in arg:
            print(ar)
            if not isinstance(ar, str):
                raise TypeError


def validate_params(func):
    def wrapper(*args, **kwargs):
        validate(args, kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper


@validate_params
def test_decorator(data_type):
    print(data_type)

test_decorator('Hello')
test_decorator('Hello', key='world')

test_decorator(2)