# Create 3 files in the classes directory car.py, fruit.py, and bank.py. Define the following classes in each module respectively. 
# Car
# Fruit
# Account
# Each class should have one class attribute and three instance variables.
# class Account:
#     bank_name = "Cooperative Bank"

#     def __init__(self, account_number, account_type, balance):
#         self.account_number = account_number
#         self.account_type = account_type
#         self.balance = balance

class Account:
    bank = "Cooperative"
    def __init__(self,account_number,withdraw,deposit):
        self.account_number = account_number
        self.withdraw = withdraw
        self.deposit = deposit
    def balance(self):
        balance_amount = self.deposit - self.withdraw
        return f"{balance_amount}"
    def open_account(self):
        return f"Yvonne opened a {self.bank} account {self.account_number} and deposited {self.deposit}ksh"
    def deposit_amount(self):
        return f"{self.deposit} was deposited to this account number {self.account_number}"