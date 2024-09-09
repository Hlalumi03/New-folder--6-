
from details import Details

class Account:
  def __init__(self, details, balance=0):
    if not isinstance(details, Details):
      raise ValueError("The 'details' argument must be an instance of the Details class.")
    self.account_holder = details.account_holder
    self.account_number = details.account_number
    self.email = details.email
    self.surname = details.surname
    self.password = details.password
    self.balance = balance
      
  def deposit(self, amount):
    if amount <= 0:
      print("Deposit amount must be positive.")
    else:
      self.balance += amount
      print(f"Deposited R{amount}. \nNew balance is R{self.balance}.")

  def withdraw(self, amount):
    if amount <= 0:
      print("Withdrawal amount must be positive.")
      
    elif amount > self.balance:
      print("Insufficient balance.")
      
    else:
      self.balance -= amount
      print(f"Withdrew R{amount}. \nNew balance is R{self.balance}.\n")

  def display_account_details(self):
    print(f"\nAccount Holder: {self.account_holder} {self.surname}")
    print(f"Email: {self.email}")
    print(f"Account Number: {self.account_number}")
    print(f"Balance: R{self.balance}\n")
