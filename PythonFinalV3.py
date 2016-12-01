import numpy as np
import csv
import os, sys

while True:
    i = int(input("Input the number of columns in this data"))
    a = i
    b = ()
    bName = ()
    while True:
        if a != 0:
            iName = (input("Input the name of the first or following element"))
            bName = bName + (iName, )
            a -= 1
            continue
        else:
            break
    while True:
        if i != 0:
            a=int(input("Input the first or following element"))
            b = b + (a,)
            i -= 1
            continue
        else:
            print(bName)
            print(b)
            break
    break

with open('outputFile.csv', 'w') as csvfile:
    oFile = csv.writer(csvfile, delimiter = ',')
    oFile.writerow(bName)
    oFile.writerow(b)
