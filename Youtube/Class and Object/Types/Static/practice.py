class Account:
    bank = "IOB"
    def __init__(self,id,name):
        self.id = id
        self.name = name
    
    def withdraw(self):
        print("Id holder name is :",self.name)
        print("Bank:",self.bank)

    def display(self):
        pass

a1 = Account(100,'Sarathy')
a2 = Account(101,'Sathish')
a1.withdraw()
a2.withdraw()