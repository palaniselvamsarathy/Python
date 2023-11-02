class Teacher:
    def __init__(self,name,number):
        self.name = name
        self.number = number

    def display(self):
        print("Teacher Name is:",self.name)
        print("Teacher Number is:",self.number)


t1 = Teacher("Sar",100)
t2 = Teacher("Sat",101)

t1.display()
t2.display()

