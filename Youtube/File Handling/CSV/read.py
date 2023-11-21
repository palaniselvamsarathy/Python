import csv

fp = open("data.csv",'r',newline="")

new = csv.reader(fp)

for i in new:
    print(i)

fp.close()

# It reads in the form of list