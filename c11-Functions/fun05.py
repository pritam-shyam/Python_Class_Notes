"""This is the fun05.py docstring."""


def f():
    return("Hello from f()")

def g():
    return("Hello from g()")

def h():
    return("Hello from h()")


a = (f, g, h)

for i in a:
    print(i)
    print(i())
