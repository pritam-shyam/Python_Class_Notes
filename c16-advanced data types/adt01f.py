data = ('one', 'two', 'three')
i = iter(data)
print(">>>>>>>>section1<<<<<<<<<")
print(next(i))
print(next(i))
print(">>>>>>>>section2<<<<<<<<<")
for x in i:
    print(x)
print(">>>>>>>>section3<<<<<<<<<")
for x in i:
    print(x)
