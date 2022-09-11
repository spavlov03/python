class Ninja: 
    def __init__(self,first_name,last_name,pet,treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet(pet,"Dog","jump")
        self.treats = treats
        self.pet_food = pet_food
    def walk(self,pet): 
        Pet.play()
    def feed(self):
        Pet.eat()
    def bathe(self,pet):
        Pet.noise()

class Pet: 
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
        print(f"{name} sound")

svet = Ninja("Svet","Pavlov","Gabi","bones","soup")
svet.feed()

