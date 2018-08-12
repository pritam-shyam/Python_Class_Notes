data1 = ('one', 'two', 'three')
data2 = ('four', 'five', 'six', 'seven')
i = zip(data1, data2) # we create an iter structure of matched pairs
print(">>>>>>>>section1<<<<<<<<<")
print(next(i)) # each call to next moves the pointer
print(next(i))
print(next(i))
print(">>>>>>>>section2<<<<<<<<<")
for a, b, in i: # note that this doesn't print anything (i is exhausted, at end)
    print(a,b)
j = zip(data1, data2) # create a new var, and get a new iter
print(">>>>>>>>section3<<<<<<<<<")
for a, b, in j:  # this one does print out the contents.
    print(a,b)
