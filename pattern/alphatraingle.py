number = int(input("Enter Number:"))

for i in range (number):
    print((chr(ord('A') + i) + ' ') * (i + 1))