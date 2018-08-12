x, y = 4, 4
twodra = [[x for x in range(x)] for y in range(y)]
print(twodra)
for i in range(len(twodra)):
    for j in range(len(twodra[i])):
        print(twodra[i][j])
