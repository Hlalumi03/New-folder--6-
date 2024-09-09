import re

#validate name
def validate_name(account_holder):
    if not account_holder.isalpha():
        print("Invalid first name")
        return account_holder

#validate surname
def validate_surname(surname):
    if not surname.isalpha():
        print("Invalid last name")
        return surname

#validate email
def validate_email(email):
    if not re.match(r"^[\w.-]+@[\w.-]+\.\w+$", email):
        print("Invalid E-mail format.")
        return email


#validate password
def validate_password(password, conf_password):
    special_symbols = ['@', '.', '#', '%']
    val = True

    if not (6 <= len(password) <= 13):
      print('Length should be between 6 and 13 characters.')
      val = False

    if not any(char.isdigit() for char in password):
      print('Password should have at least one numeral')
      val = False

    if not any(char.isupper() for char in password):
      print('Password should have at least one uppercase letter')
      val = False

    if not any(char.islower() for char in password):
      print('Password should have at least one lowercase letter')
      val = False

    if not any(char in special_symbols for char in password):
      print('Password should have at least one symbols @.#%')
      val = False

    else:
        if conf_password != password:
            print("Passwords do not match. Please try again.")
            return validate_password(password, conf_password)

    return val


