#Print inverted right angle triangle using number
number = int(input("Enter rows:"))

for i in range(number,0,-1):
    for j in range(1,i+1):
        print(j, end =' ')
        
    print()