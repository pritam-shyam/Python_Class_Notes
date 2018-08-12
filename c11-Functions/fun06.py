from sys import argv

def a():
    return("Alpha")
def b():
    return("Beta")
def c():
    return("Gamma")
def d():
    return("Delta")
def unkown():
    return("ERROR")

switcher = { 'A': a, 'a': a, 'B': b, 'b': b, 'C': c, 'c': c, 'D': d, 'd': d}

s = ''
for i in range(1, len(argv)):
    s = s + switcher.get(argv[i], unkown)() + ","
    if i == len(argv)-1:
        s = s[:-1]
print(s)
