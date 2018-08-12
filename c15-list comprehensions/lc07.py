numbers = [12,13,234,556,23123,34,567,89]

m3s_sqr = [x**2 for x in numbers if x % 3 == 0]
m3s_cub = [x**3 for x in numbers if x % 3 == 0]
m3s_qua = [x**4 for x in numbers if x % 3 == 0]

print(m3s_sqr)
print(m3s_cub)
print(m3s_qua)
