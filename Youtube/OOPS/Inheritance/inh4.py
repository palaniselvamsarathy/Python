# Hierarchical Inheritance
class Parent:
    def m1(self):
        print("Sarathy")

class C1(Parent):
    pass

class C2(Parent):
    pass

class C3(Parent):
    pass

son1 = C1()
son2 = C2()
son3 = C3()

son1.m1()
son2.m1()
son3.m1()