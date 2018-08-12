from time import sleep

def sqrList(start=0, count=0):
    data = []
    for i in range(start,start+count):
        data.append(i**2)
    return(data)

data = []
for i in sqrList(10**6, 10**9):
    if i % 1024 == 0:
        data.append(i)
print("There were ", len(data), " instances found. ")
sleep(5)  # sleep 5 seconds, to assis in monitoring memory
