class Phone:
    def __init__(self,brand,price,chargerType):
        self.brand = brand
        self.price = price
        self.chargerType = chargerType

    def display(self):
        print("Brand:",self.brand)
        print("Price:",self.price)
        print("Charger:",self.chargerType)

samsung = Phone("Samsung","50000","B-Type")
redmi = Phone("Redmi","20000","C-Type")

samsung.display()

redmi.display()

# Whenever the "Self" keyword occurs it is instance variable
# The Method is called as Instance Method
