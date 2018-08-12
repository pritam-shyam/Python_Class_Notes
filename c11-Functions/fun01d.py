def manyf(x,y=1, *args):
    print("x = %s" %(x))
    print("y = %s" %(y))
    if len(args) > 0:
        print("the rest  = %s" %(list(args)))

manyf(10)
manyf(10, 11)
manyf(10, 11, 12, 134)
