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
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0: 
            self.balance = (self.balance*self.int_rate) + self.balance
        return self
    @classmethod
    def print_all_accounts(cls):
        for account in cls.accounts: 
            account.display_account_info()

class User:
    def __init__(self, first_name,last_name,email,age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0
        self.checking_account = BankAccount(int_rate=0.01,balance=0)
        self.savings_account = BankAccount(int_rate=0.02,balance=0)
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
    def make_deposit(self,amount): 
        self.checking_account.deposit(amount)
    def make_withdrawal(self,amount):
        self.checking_account.withdrawal(amount)
    def display_user_balance(self): 
        print(f"Your {self.checking_account}")
        self.checking_account.display_account_info
    #def transfer_money(self,amount):
    #    self.checking_account.withdrawal(amount)
        #other_user.checking_account +=amount

svet_user = User("Svet","Pavlov","svet@svet.com",34)
svet_user.savings_account.deposit(18).yield_interest()
svet_user.checking_account.deposit(19).withdrawal(2)
pavel_user = User("Pavel","Skenderov","pavel@email.com",36)
pavel_user.savings_account.deposit(500).yield_interest()
pavel_user.checking_account.deposit(109).withdrawal(2)
BankAccount.print_all_accounts()


