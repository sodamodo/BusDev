__author__ = 'ZBNOAH2811'
import csv
reader = csv.reader(open("ttest.csv", "rb"))
writer = csv.writer(open("format.csv", "wb"), delimiter=',')


for row in reader:
    writerow = []
    writerow.append(row[0])
    writerow.append(row[1])
    writerow.append(float(row[3])/100000)
    writerow.append(float(row[2])/100000)
    writer.writerow(writerow)

print("fin!")