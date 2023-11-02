class Calcultor:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)
    def mul(self):
        print(self.a*self.b)
    def div(self):
        print(self.a/self.b)

calc = Calcultor(10,20)
        
calc.add()
calc.sub()
calc.mul()
calc.div()
