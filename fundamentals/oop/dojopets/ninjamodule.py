import petmodule

class Ninja: 
    def __init__(self,first_name,last_name,pet,treats,pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = petmodule.Pet_class(pet,"TEST","jump")
        self.treats = treats
        self.pet_food = pet_food
    def walk(self): 
        self.pet.play()
    def feed(self):
        self.pet.eat()
    def bathe(self):
        self.pet.noise()

svet = Ninja("Svet","Pavlov",petmodule.Cats("Gabi","TESTER","strings"),"milk","mice")
print(f"{svet.pet.name.name} is a {svet.pet.name.type} that likes to eat {svet.treats} and play with {svet.pet.name.tricks} ")
print(f"{svet.pet.name.name} Health before walk is : {svet.pet.health}")
svet.walk()
print(f"{svet.pet.name.name} Health after walk is : {svet.pet.health}")
print(f"{svet.pet.name.name} Energy & Health before feed are : {svet.pet.energy} & {svet.pet.health}")
svet.feed()
print(f"{svet.pet.name.name} Energy & Health after feed are : {svet.pet.energy} & {svet.pet.health}")
print(f"{svet.pet.name.name} Before bathe")
svet.bathe()
print(f"{svet.pet.name.name} After bathe")

pavel = Ninja("Pavel","Skende",petmodule.Dogs('Skotch','cat','catch','sticks'),'cats','bones')
print(f"{pavel.pet.name.name} is a {pavel.pet.name.type} that likes to eat {pavel.treats} and play with {pavel.pet.name.fav_toy} ")
print(f"{pavel.pet.name.name} Health before walk is : {pavel.pet.health}")
pavel.walk()
print(f"{pavel.pet.name.name} Health after walk is : {pavel.pet.health}")
print(f"{pavel.pet.name.name} Energy & Health before feed are : {pavel.pet.energy} & {pavel.pet.health}")
pavel.feed()
print(f"{pavel.pet.name.name} Energy & Health after feed are : {pavel.pet.energy} & {pavel.pet.health}")
print(f"{pavel.pet.name.name} Before bathe")
pavel.bathe()
print(f"{pavel.pet.name.name} After bathe")