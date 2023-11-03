class Player:
    def __init__(self,g_name,id,name):
        self.g_name = g_name
        self.id = id
        self.name = name

    def game(self):
        print("Game:",self.g_name)
        print("ID:",self.id)
        print("Name:",self.name)

p1 = Player("Cricket","100","Sarathy")
p2 = Player("Volleyball","101","Sathish")
p3 = Player("Foot ball","102","Shafna")
p4 = Player("Tennis","103","Rass")

p1.game()
p2.game()
p3.game()
p4.game()

# If it has self keyword then this method is Instance Method