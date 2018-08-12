def f ():
    a = 10
    print("## Namespace inside our function:")
    print(dir())
    print("## And the value of a inside our function? a=", a)

print("## Calling function...")
f()
print("## ...we're back from the function call.")
a = 20
print("## Namespace inside our program (aka: the global namespace):")
print(dir())
print("## And, finally, what is the value of a? a=", a)
