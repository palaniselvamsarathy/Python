#Print Right Angle Triangle with Sequence of Digits - each row
number = int(input("Enter rows:"))

for i in range(1,number+1):
    for j in range(1,i+1):
        print(j, end ='')
        
    print()
