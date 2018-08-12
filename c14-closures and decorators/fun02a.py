def append_to(element, to=[]):
    to.append(element)
    return to

alist=[1,2,3]
newl = append_to(to=alist, element=4)
print(newl)
print(id(newl))

newl = append_to(12)
print(newl)
print(id(newl))

newl = append_to(42)
print(newl)
print(id(newl))
