import time
t0 = time.time()
for i in range(0, 10):
    print(i)
t1 = time.time()
print("The total time to execute this loop was " + str(t1-t0))
