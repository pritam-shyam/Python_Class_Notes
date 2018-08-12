from functools import reduce
numbers = [12,13,234,556,23123,34,567,89]
out  = reduce(lambda a,b: a*b, numbers)
print(out)
