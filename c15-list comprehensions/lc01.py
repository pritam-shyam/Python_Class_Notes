numbers = [1,2,3,4,5,6,7,8]
squares = []
cubes = []
quartics = []

for number in numbers:
    squares.append(number**2)
    cubes.append(number**3)
    quartics.append(number**4)

print(numbers)
print(squares)
print(cubes)
print(quartics)
