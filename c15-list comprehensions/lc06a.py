numbers = [12,13,234,556,23123,34,567,89]

m3s_sqr = list(map(lambda x:x**2, filter(lambda x: x % 3 == 0, numbers)))
m3s_cub = list(map(lambda x:x**3, filter(lambda x: x % 3 == 0, numbers)))
m3s_qua = list(map(lambda x:x**4, filter(lambda x: x % 3 == 0, numbers)))

print(m3s_sqr)
print(m3s_cub)
print(m3s_qua)
