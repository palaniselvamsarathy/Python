import csv

fp = open('data.txt','r')

new_data = csv.reader(fp)
for line in new_data:
    print(line)
fp.close()