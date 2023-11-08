from Bank import *
class Account(Bank):
    # def __init__(self,name,id,email):
    #     self.name = name
    #     self.id = id
    #     self.email = email

    def bal(self):
        print("Account Level Balance")

    def open(self):
        print("Hey")


a1 = Account()
# print(a1)