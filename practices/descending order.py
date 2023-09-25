a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))

if a>=b and a>=c:
    if b>=c:
        print(a,b,c)
    else:
        print(c)
        print(b)
elif b>=a and b>=c:
    print(b)
    if a>=c:
        print(a)
        print(c)
    else:
        print(c)
        print(a)
        
else:
    print(c)
    if a>=b:
        print(a)
        print(b)
    else:
        print(b)
        print(a)
    
    
