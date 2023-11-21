# Polymorphism - Many forms

class Animal():
    def sound(self):
        print("Animal makes Sound")

class Dog(Animal):
    def sound(self):
        print("Dog Barks")

class Bird(Animal):
    def sound(self):
        print("Bird Sing")

# a1 = Animal()
# a1.sound()

b1 = Bird()
b1.sound()
# d1 = Dog()
# d1.sound()