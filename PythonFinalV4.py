#To get this program to work, you must first do two things before hand (this applies especially to LUC IC computers)
#Install R (I used R-3.3.2 for this version), just google install R
#Open up the command prompt and type "pip install pillow".  It shouldn't matter if pip itself is outdated, so long as pillow is in the correct directory.

import csv, os, PIL
from PIL import Image

while True:
    columns = int(input("Input the number of columns in this data (up to 2): "))
    if (columns > 2) or (columns < 1):
        print("Please enter a new number.")
        continue
    else:
        break

z = ()
y = ()
x = ()
w = () 
v = ()
u = ()
t = ()
s = ()
r = ()
q = ()
moreRows = ""
bName = ()
rows = [z, y, x, w, v, u, t, s, r, q]
numRows =  -1

a = columns


while True:
        if a != 0:
            iName = (input("Input the name of the first or following element: "))
            bName = bName + (iName, )
            a -= 1
            continue
        else:
            break
        break
    
while True:
    while True:
        numRows += 1
        i = columns
        while True:
            if numRows != 10:
                if i != 0:
                    a=float(input("Input the first or following element: "))
                    rows[numRows] = rows[numRows] + (a,)
                    i -= 1
                    continue
                else:
                    print(bName)
                    print(rows[numRows])
                    break
                break
            else:
                break
        moreRows = input("Do you wish to add more rows? (Up to 10) y/n: ")
        if moreRows == "n":
            break
        elif numRows == 10:
            break
        elif moreRows == "y":
            print(9 - numRows, " rows remaining.")
            continue
        else:
            break
    break

labels = open("graphLabels.txt", "w")

labels.write("%s \n %s\n" % (" \"" + bName[0] + "\"","\"" + bName[1] + "\""))
#I don't remember why this above line came out so messy, if I have time I'll try to clean this up.

labels.close()

with open('outputFile.csv', 'w') as csvfile:
    oFile = csv.writer(csvfile, delimiter = ',')
    oFile.writerow(bName)
    oFile.writerow(rows[0])
    oFile.writerow(rows[1])
    oFile.writerow(rows[2])
    oFile.writerow(rows[3])
    oFile.writerow(rows[4])
    oFile.writerow(rows[5])
    oFile.writerow(rows[6])
    oFile.writerow(rows[7])
    oFile.writerow(rows[8])
    oFile.writerow(rows[9])

os.system('C:\\Users\\apapaioannou\\downloads\\RScriptV2.R')

img = Image.open("C:\\Users\\apapaioannou\\documents\\rplot.jpg")
img.show()
print(img)

quit()
