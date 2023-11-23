import re
reg = input("Enter Reg NO:")

match = re.fullmatch('TN[0-9]{2}[A-Z]{2}[0-9]{4}', reg)

if match != None:
    print("Valid")

else:
    print("Not Valid")