import os
import csv
import sys

infile=sys.argv[1]
f=open(file=infile)
datalist=f.readlines()

output_file="filename.csv"

with open(output_file, 'w') as file:
    for i in range(len(datalist)):
        print(datalist[i].split()[-1])
        file.write(datalist[i].split()[-1])
        file.write("\n")
