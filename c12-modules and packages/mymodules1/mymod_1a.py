print("\n==========Hello from mymod_1a==========")

mymod_1a_str = "This string is local to mymod_1a_str"

def mymod_1a_fun():
    test_str="string local to mymod_1a_fun"
    print("==========Hello from mymod_1a_fun==========")
    print(dir())

print(dir())

print("\n==========End import of mymod_1a==========\n\n")
