class GP:
    def __init__(self):
        print("HI")
class P:
    def __init__(self):
        print("Hello")
class C(P,GP):
    def __init__(self):
        super().__init__()
    def m1(self):
        print("Hey")

child = C()
# child.__init__()
child.m1()

# It is order preserved