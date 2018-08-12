def f():
    def g():
        return("Hello from g")
    return(g)
myfun = f()
yourfun = f()
print(myfun(), '\n', yourfun(), sep='')
