number = int(input("Enter Rows:"))

for i in range(number):
    print((chr(ord('1') + i) + ' ') * (i + 1))
    
    