def func2(list):
    list += [47,11]
    print("Appended list is... " + str(list))

alist = [0,1,1,2,3,5,8]
func2(alist[:])
print("We also find that our original list was 'protected' from update...")
print(alist)
