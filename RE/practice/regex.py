import re
import csv

numbers = []
emails = []
fp = open('data.txt','r')
for line in fp:
    numbers.extend(re.compile(r'\b(?:\+\d{1,2}\s?)?(?:\d{10,12})\b').findall(line))
    emails.extend(re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b').findall(line))
fp.close()

fp1 = open('data.csv','w',newline="")
csv_writer = csv.writer(fp1)
csv_writer.writerow(['Mobile Numbers','Email IDs'])
for number,email in zip(numbers,emails):
    csv_writer.writerow([number,email])
fp1.close()

print("Done!")