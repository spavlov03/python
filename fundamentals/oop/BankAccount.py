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
    def withdraw(self, amount):
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
checking = BankAccount(0.01,100)
savings = BankAccount(0.02,200)
checking.deposit(50).deposit(25).deposit(30).withdraw(74).yield_interest().display_account_info()
savings.deposit(20).deposit(5).withdraw(65).withdraw(85).withdraw(15).withdraw(8).yield_interest().display_account_info()

BankAccount.print_all_accounts()
