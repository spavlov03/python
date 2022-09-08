class BankAccount:
    bank_name = "Svet's Bank Express"
    accounts = []
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        #self.account_type = account_type
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount < self.balance : 
            self.balance -= amount
            return self
        else: 
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
    def display_account_info(self):
        print(f" Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0: 
            self.balance += self.balance*self.int_rate
        return self
    @classmethod
    def print_all_accounts(cls): 
        for account in cls.accounts: 
            account.display_account_info()

class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = 0
        self.accounts = {}
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
    def open_new_account(self,int_rate,balance,account_type="Checking"): 
        print("Creating new account...")
        self.accounts[account_type] = BankAccount(int_rate, balance)

    def make_deposit(self,amount,account_type): 
        self.accounts[account_type].deposit(amount)
        return self
    def make_withdraw(self,amount): 
        self.accounts.withdraw(amount)
    def display_user_balance(self,account_type): 
        self.accounts[account_type].display_account_info()

svet = User("Svet","Pavlov","svet@svet.com",34)
svet.open_new_account(0.01,100,"Savings")
svet.make_deposit(10,"Savings")
svet.display_user_balance("Savings")
print(svet.accounts["Savings"][False])
