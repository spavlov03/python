class User:
    def __init__(self, first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0
    def display_info(self):
        print("First Name is: ",self.first_name)
        print("Last Name is: ",self.last_name)
        print("Email is: ",self.email)
        print("Age is: ",self.age)
        return self
    def enroll(self): 
        if self.is_reward_member == False:
            self.is_reward_member = True
        else: 
            print(f"{self.first_name} already a member.")
        self.gold_card_points = 200
        return self
    def spend_points(self,amount):
        if self.gold_card_points > amount:
            self.gold_card_points = self.gold_card_points - amount
        else: 
            print("Not Enough Points")
            #print("Your current points are :", self.gold_card_points , "you need", amount)
            print(f"Your current points are {self.gold_card_points} and you need {amount}")
        return self

svet_user = User("Svet","Pavlov","svet@svet.com",34)
mitko_user = User("Mitko","Dimitrov","mitko@gmail.com",35)
pavel_user = User("Pavel","Skenderov","pavel@maina.com",37)
svet_user.display_info().enroll().spend_points(50).enroll()
mitko_user.enroll().spend_points(80).display_info()
pavel_user.display_info().spend_points(40)




