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
        print(f"{self.name} sound")