#Hybrid Inheritance
class Dad:
    def money(self):
        print("Dad's Money")

class Land(Dad):
    def impo(self):
        print("Owner")

class Son2():
    def some(self):
        print("Hey There")

class Son(Land,Son2):
    def m1(self):
        print("Son")

son = Son()
son.impo()
son.m1()
son.money()
son.some()