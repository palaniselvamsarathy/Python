#Right Angle Triangle with sequence of Alphabets
number = int(input("Enter rows:"))

for i in range(number,0,-1):
    for j in range(i):
        print((chr(65+j)), end=' ')
    print()
        