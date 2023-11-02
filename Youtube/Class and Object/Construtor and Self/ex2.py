class laptop:
    def __init__(self,price,ram):
        print("demo")
        self.price = price
        self.ram =ram

    def display(self):
        print("Display")
        print("Ram:",self.ram)
        print("Price:",self.price)

hp = laptop(50000,'4GB')
print(hp.__dict__)
hp.display()
