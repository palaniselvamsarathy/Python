a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))

max = "a is maximum" if a>b and a>c else ("b is maximum" if b>c and b>a else "c is maximum")

print (max)