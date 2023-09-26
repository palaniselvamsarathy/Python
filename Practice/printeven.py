x = list(map(int, input("Enter multiple values: ").split()))  
print("List of students: ", x)

for i in x:
    if i%2==0:
        print(i)
    
    