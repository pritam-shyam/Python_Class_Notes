numbers = [12,13,234,556,23123,34,567,89]
m3s_sqr = []
m3s_cub = []
m3s_qua = []

for i in numbers:
    if i % 3 == 0:
        m3s_sqr.append(i**2)
        m3s_cub.append(i**3)
        m3s_qua.append(i**4)

print(m3s_sqr)
print(m3s_cub)
print(m3s_qua)
