number = int(input("Enter Number:"))
power = len(str(number))
sum = 0
temp = number
while temp>0:
    digit = temp % 10
    sum = sum + digit ** power
    temp = temp // 10

if number == sum:
    print(number, "is an Armstrong Number")
else:
    print(number, "is not an Armstrong Number")