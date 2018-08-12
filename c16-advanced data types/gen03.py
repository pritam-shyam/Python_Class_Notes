def gen_integers(start=0, count=None):
    i = start
    while True:
        yield i
        i = i + 1
        if count!=None:
            if i > start+count:
                return

def gen_squares(start=0, count=None):
    for i in gen_integers(start,count):
        yield i * i

def gen_cubes(start=0, count=None):
    for i in gen_integers(start,count):
        yield i ** 3

def gen_quatrics(start=0, count=None):
    for i in gen_integers(start,count):
        yield i ** 4

for i in gen_integers(10000, 5):
    print(i)

for square in gen_squares(10000, 5):
    print(square)

for cube in gen_cubes(10000, 5):
    print(cube)

for quatric in gen_quatrics(10000, 5):
    print(quatric)
