class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0
    def display_info(self):
        print(f"First name: {self.first_name}")
        print(f"Last name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Is enrolled: {self.is_reward_member}")
        print(f"Current points: {self.gold_card_points}")
    def enroll(self):
        if self.is_reward_member == True:
            print("User already a member.")
            return False
        else: 
            self.is_reward_member = True
            self.gold_card_points += 200
            return True
    def spend_points(self,amount):
        if amount < self.gold_card_points:
            self.gold_card_points -= amount
        else:
            print("Not Enough Points")


svet = User("Svet","Pavlov","svet@gmail.com",34)        
svet.display_info()
svet.enroll()
mitko = User("Mitko","Dimi","mitko@dimi.com",36)
pavel = User("Pavel","Skende","pavel@skende.com",38)
svet.spend_points(50)
mitko.enroll()
mitko.spend_points(80)
svet.display_info()
mitko.display_info()
pavel.display_info()
svet.enroll()
pavel.spend_points(40)

