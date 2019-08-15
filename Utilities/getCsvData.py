import csv


def getcsvdata(filename):
    rows = []
    datafile = open(filename,'r')
    reader = csv.reader(datafile)
    next(reader)
    for row in reader:
        rows.append(row)
    return rows

