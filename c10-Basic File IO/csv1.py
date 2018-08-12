"""Example reading of a csv file."""

import csv
with open('sample.csv', newline='') as csvfile:
    sampleReader = csv.reader(csvfile)
    sampleData = list(sampleReader)
    print(sampleData)
