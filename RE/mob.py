import re
mno = input("Enter Mobile Number::::")

match = re.fullmatch('[6-9]{1}[0-9]{9}', mno)

if match != None:
    print("Valid Mobile Number")
else:
    print("Not a Valid Number")