print("\n==========Hello from mymod_1b==========")

mymod_1b_str = "This string is local to mymod_1b_str"

def mymod_1b_fun():
    test_str="string local to mymod_1b_fun"
    print("==========Hello from mymod_1b_fun==========")
    print(dir())

print(dir())

print("\n==========End import of mymod_1b==========\n\n")
