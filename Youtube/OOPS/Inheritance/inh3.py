# Multi level Inheritnace
class GP:
    def m1(self):
        print("Grand Parent Method")
class P(GP):
    def m2(self):
        print("Parent Method")
class C(P):
    def m3(self):
        print("Child Method")

child = C()
child.m1()
child.m2()
child.m3()

dad = P()
dad.m1()
dad.m2()