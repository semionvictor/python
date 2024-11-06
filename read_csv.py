import csv

with open("people.csv","r") as csvFile:
    csv_read = csv.reader(csvFile)
    for line in csv_read:
        print(line)
