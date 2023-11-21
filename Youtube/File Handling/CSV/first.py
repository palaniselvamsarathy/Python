import csv
fp = open('data.csv','w',newline="")

csv_obj = csv.writer(fp)
csv_obj.writerow(['id','name','area'])

rows = int(input("Enter the rows:"))

for i in range(rows):
    id = int(input("ID:"))
    name = input("Name:")
    area = input("Area:")
    
    csv_obj.writerow([id,name,area])

fp.close()