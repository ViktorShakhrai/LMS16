# Write a class TypeDecorators which has several methods for converting results
# of functions to a specified type (if it's possible):
#
# methods:
# to_int
# to_str
# to_bool
# to_float

# Don't forget to use @wraps
#
# ```
# class TypeDecorators:
#     pass
#
#
# @TypeDecorators.to_int
# def do_nothing(string: str):
#     return string
#
# @TypeDecorators.to_bool
# def do_something(string: str):
#     return string
#
# assert do_nothing('25') == 25
#
# assert do_something('True') is True
# ```
from functools import wraps


class TypeDecorator:
    @staticmethod
    def to_int(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            rez_func = func(*args, **kwargs)
            try:
                return int(rez_func)
            except ValueError:
                print("Value int")

        return wrapper


@TypeDecorator.to_int
def f():
    return "5"

s = f()
print(s)
