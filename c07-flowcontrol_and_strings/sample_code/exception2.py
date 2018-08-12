# NOTE: This sample code is copied from https://docs.python.org/3/tutorial/errors.html

class B(Exception):  # create a subclass of Exception object
    pass

class C(B): # sublass B (whose parent is Exception object)
    pass

class D(C): # subclass C (whose granparent is Exception object)
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
