import csv
with open("input.csv") as inFile:
    csvReader = csv.reader(inFile)
    inData = list(csvReader)
    header = inData[0]
    strData = inData[1:]

out = [[row[0],row[1],row[2],row[3],float(row[1])*(1+float(row[2]))**float(row[3])] for row in strData]

with open("output.csv",'w', newline='') as outFile:
    csvWriter = csv.writer(outFile)
    header.append('FV')
    csvWriter.writerow(header)
    csvWriter.writerows(out)
