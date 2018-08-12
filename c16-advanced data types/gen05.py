def logBytes(inFileName):
    line_num = 0
    inFile = open(inFileName)
    for line in inFile:
        line_num+=1
        x = line.rsplit(None,1)[1]
        if x!='-':
            yield int(x)
    inFile.close()


for x in logBytes("access_log"):
    print("Byte={:,}".format(x) ) # note that our function now doesn't need to return the entire list in memory, just one at a time.

print('The total bytes transfered = {:,}'.format(sum(logBytes("access_log"))))
