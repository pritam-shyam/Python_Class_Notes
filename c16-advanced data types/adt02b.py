from collections import namedtuple
person = namedtuple('Person', ['first', 'last', 'address'])
tim = person('Tim','Smith', '123 Wayward Way')
print(tim.first)
print(tim.last)
print(tim.address)
jane = person('Jane', 'Smith', '21 Elm St.')
print(jane.first)
print(jane.last)
print(jane.address)
for p in [tim,jane]:
    print('%s %s lives at %s' % p)
