class MiniGoa:
    name = "Man"
    drink = ""
    place = ""

    def party(self):
        print("Let's party!!!")
        print(".....")

    def tourism(self):
        print("Explore Mini Goa!!!")
        print("....")
sathish = MiniGoa()
sarathy = MiniGoa()
rass = MiniGoa()
sathish.name = "Sathish"
sarathy.name ="Sarathy"

sathish.drink = "yes"
sarathy.drink ="no"
sarathy.tourism()
print(sarathy.name)
print("Drink: ",sarathy.drink)
sathish.party()
print(sathish.name)
print("Drink: ",sathish.drink)

# print(rass.name)
