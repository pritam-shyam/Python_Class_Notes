from collections import Iterator, Iterable
x = [1,2,3]
y = {'one': 1, 'two': 2}
z = 10
print(isinstance(x,Iterator))
print(isinstance(y,Iterator))
print(isinstance(z,Iterator))
print(isinstance(iter(x),Iterator))
print(isinstance(iter(y),Iterator))
print(isinstance(iter(z),Iterator))
