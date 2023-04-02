import os
import csv
import sys

infile=sys.argv[1]
root_dir=os.path.dirname(infile)
f=open(file=infile)
datalist=f.readlines()

output_file=os.path.join(root_dir,"eval_result.csv")

with open(output_file, 'w') as file:
    for i in range(len(datalist)):
        print(datalist[i].split()[-1])
        file.write(datalist[i].split()[-1])
        file.write("\n")
