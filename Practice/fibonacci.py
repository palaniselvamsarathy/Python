n = int(input("Enter Number:"))
first = 0
last = 1

if n < 1:
    print(first)
for x in range(1, n):
    print(last)
    temp = first + last
    first = last
    last = temp