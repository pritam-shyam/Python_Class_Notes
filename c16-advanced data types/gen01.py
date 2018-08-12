def fun1 (inFileName):
    inFile = open(inFileName)
    firstWords = []
    for line in inFile:
        words = line.split(maxsplit=1)
        if len(words) > 0:
            firstWords.append(words[0])
    inFile.close()
    return(firstWords)

for firstWord in fun1("WizardOfOz.txt"):
    print(firstWord) # note that our function now doesn't need to return the entire list in memory, just one at a time.
