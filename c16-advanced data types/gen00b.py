from time import sleep

def sqrListGen(start=0, count=0):
    for i in range(start,start+count):
        yield i**2

data = []
for i in sqrListGen(10**6, 10**9):
    if i % 1024 == 0:
        data.append(i)
print("There were ", len(data), " instances found. ")
sleep(5)  # sleep 5 seconds, to assis in monitoring memory
