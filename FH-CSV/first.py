import csv

fp = open('MOCK_DATA.csv','r')

new_data = csv.reader(fp)
for line in new_data:
    print(line)
fp.close()