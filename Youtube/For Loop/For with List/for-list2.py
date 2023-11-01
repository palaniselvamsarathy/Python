list = []
print("Enter Ten Values:")
for i in range(10):
    num = int(input("Enter Value "+str(i+1)+":"))
    list.append(num)
print(list)

sum = 0
for i in list:
    sum+=i
avg = sum/len(list)
print(sum)
print(avg)

