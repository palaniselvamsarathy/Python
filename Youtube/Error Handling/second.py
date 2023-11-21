try:
    a= int(input(""))
    b= int(input(""))
    print(a+b)

except ValueError as err:
    print(err)
