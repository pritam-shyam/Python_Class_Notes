
def f():
    """This function simply prints a message. """
    print("This is MIS407.")

print(isinstance(f, object))  # is this an instance of an object

print(id(f))  # like we've seen before, name of objects are simply ID/pointers

print(f.__doc__)  # print the docstring for the function
print(f.__name__)  # print the name of the function
