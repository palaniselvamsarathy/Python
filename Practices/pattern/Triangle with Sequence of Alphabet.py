#.Print Right Angle Triangle with Sequence of Alphabet - each row

number = int(input("Enter row:"))
for i in range(1,number+1):
    for j in range(i):
        print(chr(65+j), end =' ')
    print()