#  Outer and inner functions


# def outer_func(msg):
#     def inner_func():
#         print(msg)
#
#     return inner_func
#
#
# hi_func = outer_func("hi")
# bye_func = outer_func("bye")


# hi_func()
# bye_func()

# Decorator


def decorator_func(original_func):
    def wrapper_func(*args, **kwargs):
        print("Wrapper func executed before {}".format(original_func.__name__))
        return original_func(*args, **kwargs)

    return wrapper_func


# @decorator_func
# def display_func():
#     print("original func ran")


# @decorator_func
# def display_info(name, age, is_married=False):
#     print("Name : {}, Age {}".format(name, age))
#     if is_married:
#         print("{} is married".format(name))


# display_info(name='John', age=25, is_married=True)

# Decorator class


class DecoratorClass(object):
    def __init__(self, original_func):
        self.original_func = original_func

    def __call__(self, *args, **kwargs):
        print("call method executed before {}".format(self.original_func.__name__))
        return self.original_func(*args, **kwargs)


@DecoratorClass
def display_info(name, age, is_married=False):
    print("Name : {}, Age {}".format(name, age))
    if is_married:
        print("{} is married".format(name))


display_info('John', 24, True)
