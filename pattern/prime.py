number =int(input("Enter value:"))

if number ==1:
    print("Prime")
elif number>=2:
    for i in range(2,number):
        if number%i==0:
            print("Not a Prime")
            break
    else:
        print("Prime")
        
else:
    print("Not a Prime")