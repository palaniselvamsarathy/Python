#Print Inverted Right Angle Triangle using sequence number in descending order

number =int(input("Enter rows:"))

for i in range(number,0,-1):
    for j in range(number,number-i,-1):
        print(j, end =' ')
    print()