class User:
    def __init__(self, name="Unassigned"):
        self.name = name
        self.accounts = {}
    def open_new_account(self, with_amount=0,interest=0.04,account_type="checking"):
        print("Creating new account...")
        self.accounts[account_type] = BankAccount(with_amount,interest,account_type)
        return self
    def make_withdrawal(self,amount, account_type="checking"):
        self.accounts[account_type].withdraw(amount)
        return self
    def display_user_balance(self): 
        print(self.name)
        for account_name in self.accounts:
            self.accounts[account_name].display_account_info()
        return self
    def transfer_money(self,other_user,other_user_acc_type,amount,from_account_type):
        if self.accounts[from_account_type].balance < amount:
            print("Insuficient funds")
            return self
        print(f"Transferring $ {amount} into {other_user.name}'s {other_user_acc_type} account,")
        self.accounts[from_account_type].balance -= amount
        other_user.accounts[other_user_acc_type].balance += amount
        self.display_user_balance()
        other_user.display_user_balance()

        return self
    def make_deposit(self,amount, account_type="checking"): 
        self.accounts[account_type].deposit(amount)
        return self
    def yielf_interest(self):
        self.account.yield_interest()
        return self 

class BankAccount:
    bank_name = "First National Dojo"
    all_accounts = []
    def __init__(self, balance=0, interest=0.01, account_type="checking"): 
        self.balance = balance 
        self.interest = interest
        self.account_type = account_type
        BankAccount.all_accounts.append(self)
    def deposit(self, amount):
        print(f"Depositing $ {amount}")
        self.balance = self.balance + amount
        return self
    def withdraw(self, amount):
        if self.balance >= amount: 
            self.balance = self.balance-amount
        else: 
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self
    def display_account_info(self):
        print(f"Account : {self.account_type}")
        print(f"Account Balance: ${self.balance}")
        print(f"Interest Rate: {self.interest}")
        return self
    def yield_interest(self):
        if self.balance > 0: 
            print("Yielfind interest...")
            self.balance = (self.balance*self.int_rate) + self.balance
        return self
    @classmethod
    def print_all_accounts(cls):
        for account in cls.all_accounts: 
            account.display_account_info()
        return cls
svet = User("Svet Pavlov")
svet.open_new_account(0,0.05)
svet.make_deposit(100)
svet.open_new_account(500,0.06,"savings")

mitko = User("Mitko Dimi")
mitko.open_new_account(300,0.045)
#svet.display_user_balance()
#mitko.display_user_balance()

mitko.transfer_money(svet,"checking",100,"checking").make_withdrawal(150)

