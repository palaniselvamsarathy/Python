from Account import *

class CA (Account):
    def __init__(self,name,id,email,loc):
        super().__init__(name,id,email)
        self.loc = loc

    def get_money(self):
        print("Hey There")

cal1 = CA("sarathy",102,"xyz@gmail.com","Bangalore")
print(cal1.__dict__)