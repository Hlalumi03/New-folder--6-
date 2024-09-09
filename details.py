import hashlib
import random as r

#Not used yet
def hash_password(password):
  return hashlib.sha256(password.encode()).hexdigest()
  
def _gen_account_number(existing_numbers):
  while True:
    number = 1620000 + r.randint(10000, 99999)
    if number not in existing_numbers:
      existing_numbers.add(number)
      return number

class Details:
  def __init__(self, account_holder, surname, email, password, account_number=None):
    self.account_holder = account_holder
    self.surname = surname
    self.email = email
    self.password = str(password)
    self.account_number = account_number if account_number is not None else _gen_account_number(Details.existing_account_numbers)

  existing_account_numbers = set()
  
  def __str__(self):
    return (
      f'Name: {self.account_holder}\n'
      f'Surname: {self.surname}\n'
      f'Email: {self.email}\n'
      f'Password: {self.password}\n'
      f'Account Number: {self.account_number}\n'
      + "_" * 30 + "\n"
    )

  def save_to_file(self, filename="details.txt"):
      try:
        with open(filename, "a") as file:
          file.write(self.__str__())
      except Exception as e:
        print(f'An error has occurred while saving file: {e}')

  @staticmethod
  def read_from_file(filename="details.txt"):
    try:
      with open(filename, "r") as file:
        return file.read()
      
    except FileNotFoundError:
      print(f'The file {filename} does not exist.')
      return None
  
    except Exception as e:
      print(f'An error occurred while reading from file: {e}')
      return None