


class BankAccount:
    accounts = []
    def __init__(self, int_rate=0.01, balance=0): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount < self.balance : 
            self.balance += amount
            return self
        else: 
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
            return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0: 
            self.balance += self.balance*self.int_rate
        return self
    @classmethod
    def print_all_accounts(cls): 
        for account in cls.accounts: 
            account.display_account_info()

checking = BankAccount(0.02,100)
savings = BankAccount(0.05,50)
checking.deposit(20).deposit(25).deposit(7).yield_interest().display_account_info()
savings.deposit(15).deposit(3).withdraw(20).withdraw(10).withdraw(7).withdraw(35).display_account_info()

BankAccount.print_all_accounts()
