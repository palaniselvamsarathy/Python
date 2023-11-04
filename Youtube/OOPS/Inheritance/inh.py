#Single Level Inheritance
class Parent:
    # def __init__(self):
    #     pass

    def m1(self):
        print("M1 method")

    def m2(self):
        print("M2 method")

class Child(Parent):
    def m4(self):
        print("Child M4 method")

son = Child()
son.m1()
son.m2()
son.m4()
    