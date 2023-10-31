import csv

fp = open('user.csv','w',newline="")

csv_obj = csv.writer(fp)
csv_obj.writerow(['id','name','city'])

no_of_rows = int(input("Enter the Number of rows:"))

for x in range(no_of_rows):
    id = int(input("Enter ID:"))
    name = input("Enter Name:")
    city = input("Enter City:")
    csv_obj.writerow([id,name,city])

fp.close()