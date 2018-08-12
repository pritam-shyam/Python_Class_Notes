"""Example reading of a csv file."""

import csv
with open ('sample.csv') as csvFile:
    sampleReader = csv.reader(csvFile)
    for row in sampleReader:
        print('Row #' + str(sampleReader.line_num) + ": " + str(row[0]))
