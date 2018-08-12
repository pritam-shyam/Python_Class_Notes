"""Example reading of a csv file."""

import csv
with open('sample.csv', newline='') as csvfile:
    sampleReader = csv.reader(csvfile)
    sampleData = tuple(sampleReader)
print(sampleData[0][0], ": ", sampleData[1][0], sep='')
print(sampleData[0][1], ": ", sampleData[1][1], sep='')
