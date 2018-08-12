def func2(list):
    list += [47,11]
    print("This is an appended list " + str(list))
    return(None)

alist = [0,1,1,2,3,5,8]
func2(alist)
print("But the original list we sent to the function wasn't protected, and thus altered... ")
print(alist)
