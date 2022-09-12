import petmodule

class Ninja: 
    def __init__(self,first_name,last_name,pet,treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = petmodule.Pet_class(pet,"Dog","jump")
        self.treats = treats
        self.pet_food = pet_food
    def walk(self): 
        
        self.pet.play()
    def feed(self):
        self.pet.eat()
    def bathe(self):
        self.pet.noise()

svet = Ninja("Svet","Pavlov","Gabi","bones","soup")
print(f"Health before walk is : {svet.pet.health}")
svet.walk()
print(f"Health after walk is : {svet.pet.health}")
print(f"Energy & Health before feed are : {svet.pet.energy} & {svet.pet.health}")
svet.feed()
print(f"Energy & Health after feed are : {svet.pet.energy} & {svet.pet.health}")
print(f"Before bathe")
svet.bathe()
print(f"After bathe")

