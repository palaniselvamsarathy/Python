class laptop():
    chargerType = "B-TyPE"
    tax = "hEY"
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
    @staticmethod
    def info():
        print("This is the INformation of Laptop")
hp = laptop("hp","20000")
# hp.setPrice(50000)
# hp.getPrice()

# laptop.changeChargerType()

# laptop.info()

laptop.cal_tax()
