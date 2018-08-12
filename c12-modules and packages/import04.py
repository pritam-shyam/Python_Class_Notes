from time import time as tmr
t0 = tmr()
for i in range(0, 10):
    print(i)
t1 = tmr()
print("The total time to execute this loop was " + str(t1-t0))
