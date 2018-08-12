def f(x):
    def g():
        print(x)
    return(g)

fnc1 = f(2)
fnc2 = f(100)

fnc1()
fnc2()
