# Multiple Inheritance
class Parent1:
    def m1(self):
        print("Parent - 1 m1 method")

    def m2(self):
        print("Parent - 1 m2 method")

class Parent2:
    def m3(self):
        print("Parent 2 m3 method")

class Son(Parent1,Parent2):
    def m4(self):
        print("Child level method")

child = Son()

child.m1()
child.m2()
child.m3()
child.m4()