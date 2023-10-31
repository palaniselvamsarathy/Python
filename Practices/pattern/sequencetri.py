number = int(input("Enter Rows:"))

for i in range(number):
    for j in range(i +1):
        print((chr(ord('1') + i) + ' ') * (i + 1))
        
    print()
        
#     print((chr(ord('1') + i) + ' ') * (i + 1))