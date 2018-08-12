def manyf(x,y=1, **kwargs):
    print("x = %s" %(x))
    print("y = %s" %(y))
    if 'a' in kwargs:
        print('a = %s ' % kwargs['a'])
    if 'b' in kwargs:
        print('a = %s ' % kwargs['b'])
    print(kwargs)

manyf(10)
manyf(10, 11)
manyf(x=10, y=11, a=12, b=134)
