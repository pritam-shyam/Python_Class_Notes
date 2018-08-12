def cache_this(element, to=[]):
    to.append(element)
    return to

cache = cache_this(12)
print(cache)
print(id(cache))

cache = cache_this(42)
print(cache)
print(id(cache))
