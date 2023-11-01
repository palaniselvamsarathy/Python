salary = int(input("Salary:"))
age = int(input("Age:"))

if(salary>= 20000 or age<=25):
    loan = int(input("Loan:"))
    if (loan<=50000):
        print("You are Eligible for loan")
    else:
        print("The maximum loan amount is 50000")
else:
    print("You are Not Eligible for loan")