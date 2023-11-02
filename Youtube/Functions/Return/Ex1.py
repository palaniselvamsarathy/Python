uname = input(":")
password = input(":")

def validate(uname,password):
    s_username = "EMC"
    s_password = "123"

    if(uname == s_username and password == s_password):
        return True
    else:
        return False
    
a = validate(uname,password)
print(a)