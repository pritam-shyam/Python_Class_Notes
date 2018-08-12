def cache_this(element, to=[1,2,3]):
    to.append(element)
    return to

cache = cache_this(12)
print(cache)
print(id(cache))

cache = cache_this(42)
print(cache)
print(id(cache))
