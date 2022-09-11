class User:
    def __init__(self, first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0
        self.accounts = {"checking":BankAccount(0.02,0), "savings":BankAccount(0.05,0)}
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
    def make_deposit(self,amount,acc_type): 
        self.accounts[acc_type].deposit(amount)
        return self
    def make_withdrawal(self,amount,acc_type):
        self.accounts[acc_type].withdrawal(amount)
        return self
    def display_user_balance(self,acc_type): 
        #print(f"Your {self.accounts[acc_type]}")
        self.accounts[acc_type].display_account_info(acc_type,self.first_name)
        return self
    def transfer_money(self,amount,my_account_type,other_user,other_user_acc_type):
        if self.accounts[my_account_type].balance > amount: 
            print(f"Transferring ${amount} from {self.first_name}s {my_account_type} to {other_user.first_name}s {other_user_acc_type} account")
            self.accounts[my_account_type].withdrawal(amount)
            other_user.accounts[other_user_acc_type].deposit(amount)
            print("Transfer Completed")
            print(f"{self.first_name}s {my_account_type} balance is now ${self.accounts[my_account_type].balance}")
            print(f"{other_user.first_name}s {other_user_acc_type} balance is now ${other_user.accounts[other_user_acc_type].balance}")
        else: 
            print("Insufficient funds")
        return self



class BankAccount:
    bank_balance = 0
    accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance 
        BankAccount.bank_balance += balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance = self.balance + amount
        return self
    def withdrawal(self, amount):
        if self.balance >= amount: 
            self.balance = self.balance-amount
        else: 
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self,acc_type,first_name):
        print(f"{first_name} {acc_type} account balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0: 
            self.balance = (self.balance*self.int_rate) + self.balance
        return self


svet = User("Svet","Pavlov","svet@svet.com",34)
svet.make_deposit(10,"checking").make_withdrawal(2,"checking").display_user_balance("checking")
pavel = User("Pavel","Skenderov","pavel@email.com",36)
pavel.make_deposit(10,"checking").make_deposit(15,"savings").display_user_balance("checking")
svet.transfer_money(15,"checking",pavel,"checking")



