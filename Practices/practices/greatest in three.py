a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))

if a > b and a > c:
    print(a, " is Greatest")
    
elif b>c and b>a:
    print(b, "is Greatest")
    
else:
    print(c, " is Greatest")