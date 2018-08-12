import sys

def sqr(args):
    if len(args) != 1:
        return('ERROR: sqr only accepts one value')
    return(float(args[0])**2)

def sqrt(args):
    if len(args) != 1:
        return('ERROR: sqrt only accepts one value')
    return(float(args[0])**(1/2))

def cube(args):
    if len(args) != 1:
        return('ERROR: cube only accepts one value')
    return(float(args[0])**3)

def cubert(args):
    if len(args) != 1:
        return('ERROR: cubert only accepts one value')
    return(float(args[0])**(1/3))

def unkown(args):
    return("ERROR: Unkown command. Please choose one of SQR, SQRT, CUBE, CUBERT")

switcher = { 'SQR': sqr, 'SQRT': sqrt, 'CUBE': cube, 'CUBERT': cubert}

s = ''
if len(sys.argv)>1:
    s = switcher.get(sys.argv[1], unkown)(sys.argv[2:])
print(s)
