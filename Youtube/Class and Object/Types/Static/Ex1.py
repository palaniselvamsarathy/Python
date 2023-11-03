class Phone:
    chargerType = "C-Type"  # Static Variable
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Charger:",self.chargerType)

    def dis(cls):
        cls.chargerType = "B"
        print("Changed")
# Phone.chargerType = "B-TYPE"
samsung = Phone("Samsung","50000")
redmi = Phone("Redmi","20000")

# samsung.display()
# redmi.display()
samsung.dis()