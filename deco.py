# -*-coding:utf-8-*-
# /usr/bin/env python
# Author: jiucheng
# Date: 7/27/17

def deco(func):
    """dasda"""

    def wraper():
        """dasda"""
        print("before myfun() called")
        func()
        print("after myfunc() called")
        return func

    return wraper


#
# def deco(f):
#     """decottt"""
#     print("test")
#     f()
#     return f


@deco
def myfunc():
    """nisi"""
    print("my func() called")


# myfunc()
# a = deco(myfunc)

def decorator_maker():
    print("I make decorators! I am executed only once: " + \
          "when you make me create a decorator.")

    def my_decorator(func):
        print(
            "I am a decorator! I am executed only when you decorate a function.")

        def wrapped():
            print("I am the wrapper around the decorated function. "
                  "I am called when you call the decorated function. "
                  "As the wrapper, I return the RESULT of the decorated function.")
            return func()

        print("As the decorator, I return the wrapped function.")

        return wrapped

    print("As a decorator maker, I return a decorator")
    return my_decorator


# new_decorator = decorator_maker()
#
# def decorated_function():
#     print ("I am the decorated function.")

# decorated_function = new_decorator(decorated_function)

# decorated_function()

# decorated_function = decorator_maker()(decorated_function)
#
# print('next')
# decorated_function()

# @decorator_maker()
# def decorated_function():
#     print ("I am the decorated function.")

# decorated_function()
def decorator_maker_with_arguments(decorator_arg1, decorator_arg2):
    print("I make decorators! And I accept arguments:", decorator_arg1,
          decorator_arg2)

    def my_decorator(func):
        # 这里之所有可以传递参数，得益于closures的特性。
        # 如果你不熟悉closures,你可以假设这是没问题的，
        # 或者读一下: http://stackoverflow.com/questions/13857/can-you-explain-closures-as-they-relate-to-python

        print("I am the decorator. Somehow you passed me arguments:",
              decorator_arg1, decorator_arg2)

        # 不要把装饰器的参数和函数的参数搞混
        def wrapped(function_arg1, function_arg2):
            print("I am the wrapper around the decorated function.\n"
                  "I can access all the variables\n"
                  "\t- from the decorator: {0} {1}\n"
                  "\t- from the function call: {2} {3}\n"
                  "Then I can pass them to the decorated function"
                  .format(decorator_arg1, decorator_arg2,
                          function_arg1, function_arg2))
            return func(function_arg1, function_arg2)

        return wrapped

    return my_decorator


@decorator_maker_with_arguments("Leonard", "Sheldon")
def decorated_function_with_arguments(function_arg1, function_arg2):
    print("I am the decorated function and only knows about my arguments: {0}"
          " {1}".format(function_arg1, function_arg2))


print("next")

decorated_function_with_arguments("Rajesh", "Howard")
