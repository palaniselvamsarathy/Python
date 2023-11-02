class Student:
    def __init__ (self,name,number):
        self.name = name 
        self.number = number

    def display(self):
        print("Name:",self.name) 
        print("Number:",self.number)
a = input(":")
b = int(input(":"))
s1 = Student(a,b)

print(s1.name)
print(s1.number)
s1.display()
