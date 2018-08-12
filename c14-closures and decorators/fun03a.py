def f(x):
    print(id(x)) # id(x) returns the id of the 123 object
    return(x)

x=10
print(id(x))
print(id(10)) # note that id(x) and id(10) return the same value
print( id( f(10) ) )
x=123
print(id(x))
print(id(123)) # note that id(x) and id(10) return the same value
print( id( f(123) ) )
