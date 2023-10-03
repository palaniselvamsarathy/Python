# * * * * *
# * * * *
# * * *
# * *
# *

number = int(input("Enter Row:"))
print()
for i in range(number,0,-1):
    for j in range(i):
        print("*", end = " ")
    print()
        