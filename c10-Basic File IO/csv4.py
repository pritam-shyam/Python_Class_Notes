"""Example reading of a csv file."""

import csv
csvFile = open('sample.csv')
sampleReader = csv.reader(csvFile)
for row in sampleReader:
    print('Row #' + str(sampleReader.line_num) + ": " + str(row[0]))
