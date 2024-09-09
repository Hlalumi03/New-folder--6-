from details import hash_password
from account import Account

class AccountManager:
  accounts = {}

  @staticmethod
  def create_account(details, balance=0):
    if details.email in AccountManager.accounts:
      print(f"Account with email {details.email} already exists.")
      return None
                  
    account = Account(details, balance)
    AccountManager.accounts[details.email] = account
    print(f"Account created for {details.account_holder}.")
    return account
  
  @staticmethod
  def get_account(email):
    return AccountManager.accounts.get(email)

  @staticmethod
  def sign_in(email, password):
    account = AccountManager.get_account(email)
    if account and account.password == hash_password(password):
      return account
    return None