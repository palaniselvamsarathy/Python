list=[]
n= int(input("Enter Range:"))
sum=0
for i in range(1,n+1):
    list.append(i)
for i in list:
    sum+=i
print(list)
print(sum)