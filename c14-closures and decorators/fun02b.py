def append_to(element, to=[]):
    to.append(element)
    return to

newl = append_to(12)
print(newl)
print(id(newl))

newl = append_to(42)
print(newl)
print(id(newl))
