class Pet_class: 
    def __init__(self,name,type,tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 0
        self.health = 0
    def sleep(self):
        self.energy += 25
    def eat(self):
        self.energy += 5
        self.health += 10
    def play(self):
        self.health +=5
    def noise(self):
        print(f"{self.name.name} sound")

class Dogs(Pet_class):
    def __init__(self, name, type, tricks, fav_toy):
        super().__init__(name, type, tricks)
        self.fav_toy = fav_toy
        self.type = "Dog"
    def fetch(self): 
        print("Get the ball boy!")

class Cats(Pet_class):
    def __init__(self, name, type, tricks):
        super().__init__(name, type, tricks)
        self.type = "Cat"
    def fetch(self):
        print("here kitty kitty")