def manyf(x,y=1, *args):
    print("x = %s" %(x))
    print("y = %s" %(y))
    if 'a' in args:
        print('a = %s ' % args['a'])
    if 'b' in args:
        print('a = %s ' % args['b'])
    print(args)

manyf(10)
manyf(10, 11)
manyf(x=10, y=11, 12, 134)
