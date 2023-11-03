class laptop():
    chargerType = "B-TyPE"
    def __init__(self,brand,price):
        self.brand = brand
        self.price = price

    def setPrice(self,price):
        self.price = price

    def getPrice(self):
        print(self.price)

    @classmethod
    def changeChargerType(cls):
        cls.chargerType = "C-TYPE"
        print("Changed")

hp = laptop("hp","20000")
hp.setPrice(50000)
hp.getPrice()

laptop.changeChargerType()

# By using Decorator we are not gonna give the object


# Whichever using Cls keyword is Classs Method

# We have to add one decorator in Class Method

# We have to call this using Class Name