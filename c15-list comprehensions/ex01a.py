import csv
with open("input.csv") as inFile:
    csvReader = csv.reader(inFile)
    inData = list(csvReader)
    header = inData[0]
    strData = inData[1:]

floatData = [[float(y) for y in x] for x in strData]
out = [[x[0],x[1],x[2],x[3],x[1]*(1+x[2])**x[3]] for x in floatData]

with open("output.csv",'w', newline='') as outFile:
    csvWriter = csv.writer(outFile)
    header.append('FV')
    csvWriter.writerow(header)
    csvWriter.writerows(out)
