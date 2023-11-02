class Account:

    def __init__(self,id,name):
        self.acc_id = id
        self.acc_name  = name 
        

    def deposit(self):
        print("Your Amount is deposited")

# a1 = Account()
# a1.deposit()
#
a2 = Account(101,'Sarathy')
a3 = Account(102,'Sathish')
a4 = Account(103,'Rass')

print(a2.__dict__)
print(a3.__dict__)
print(a4.__dict__)