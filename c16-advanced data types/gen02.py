
def gen_firstWords (inFileName):
    inFile = open(inFileName)
    for line in inFile:
        words = line.split(maxsplit=1)
        if len(words) > 0:
            yield words[0]
    inFile.close()

for firstWord in gen_firstWords("WizardOfOz.txt"):
    print(firstWord) # note that our function now doesn't need to return the entire list in memory, just one at a time.

listOfFirstWords= list(gen_firstWords("WizardOfOz.txt")) # I could put this all in memory if I wanted to.
