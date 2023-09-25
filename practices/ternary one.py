a = int(input("Enter First Number:"))
b = int(input("Enter Second Number:"))
c = int(input("Enter Third Number:"))

min = "a is minimum" if a<b and a<c else ("b is minimum" if b<c and b<a else "c is minimum")

print (min)