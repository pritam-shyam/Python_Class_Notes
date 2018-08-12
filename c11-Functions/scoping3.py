
def outer_function():
    # remove the nonolocal call here to make code work (and see what the difference is versus global)
    nonlocal a ## this will result in the inner_function call havning nothin to bind to in this nonlocal (but nonglobal) context, and thus will generate and error.
    a = 20
    def inner_function():
        nonlocal a
        a = 30
        print('a =', a)

    inner_function()
    print('a =', a)
a = 10
outer_function()
print('a =', a)
