a =int(input("Enter The First Number"))
b = int(input("Enter the Second Number"))

calc = input("Enter The operation(ADD/SUB/MUL/DIV):")

if(calc == "ADD"):
    print("Addition of ",a,"and",b,"is",a+b)

elif(calc== "SUB"):
    print("Subtraction of ",a,"and",b,"is",a-b)

elif(calc == "MUL"):
    print("Multiplication of ",a,"and",b,"is",a*b)

elif(calc == "DIV"):
    print("Division of ",a,"and",b,"is",a/b)

else:
    print("Enter valid Format such as (ADD,SUB,MUL,DIV)")