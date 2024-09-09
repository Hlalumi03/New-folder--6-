from details import Details
from account import Account
from account_manager import AccountManager
from utils import validate_name, validate_surname, validate_email, validate_password

#Modified acc creation
def create_account():
    while True:
        account_holder = input("Enter Your First Name: ").capitalize()
        if validate_name(account_holder):
            continue
        else:
            break

    while True:
        surname = input("Enter Your Last Name: ").capitalize()
        if validate_surname(surname):
            continue
        else:
            break

    while True:
        email = input("Enter Your E-mail: ")
        if validate_email(email):
            continue
        else:
            break

    while True:
        password = input("Enter a password: ")
        conf_password = input("Confirm password: ")
        print("Almost there...")
        if validate_password(password, conf_password):
            details = Details(account_holder=account_holder, surname=surname, email=email, password=password)
            details.save_to_file()
            client = Account(details)
            starting_balance(client)
            print("Account created successfully!. \n")
            print(f"Welcome {account_holder}, here are your details.")
            #client.display_account_details()
            menu(client)

        else:
            print("Failed to create account due to validation errors.")
        break

#Starting Amount
def starting_balance(user):
    while True:
        print("You need a minimum starting balance of R20 to any amount you would like!.\n")
        amount = float(input("Enter Starting amount: R"))
        if amount <= 10:
            print("Deposit amount has to be above R10.")
        else:
            user.deposit(amount)
            break

def sign_in():
    while True:
        email = input("\nEnter your email: ")
        password = input("Enter your password: ")

        account = AccountManager.sign_in(email, password)
        if account:
            print("Sign in successful! \n")
            account.display_account_details()
            menu(account)
            break

        else:
            print("\nNo account found with provided details. \n"
                "Would you like to create an account? \n"
                "1. Yes \n"
                "2. No \n"
                "3. Try again\n")

            x = input("Enter here: ")

            if x == '1':
                create_account()
                break

            elif x == '2':
                print("Thank you for using Bank Manager")
                break

            elif x == '3':
                continue

            else:
                print("Invalid option. Please enter 1, 2 or 3.")

def menu(account):
    while True:
        print("Bank Account Manager.\n"
            "1. Deposit.\n"
            "2. Withdraw.\n"
            "3. Display Account details.\n"
            "4. Exit.\n")

        choice = input("Enter your choice: ")

        if choice in {"1", "2", "3", "4"}:
            try:
                if choice == '1':
                    amount = float(input("Enter amount: R"))
                    account.deposit(amount)

                elif choice == '2':
                    amount = float(input("Enter the amount to withdraw: R"))
                    account.withdraw(amount)

                elif choice == '3':
                    account.display_account_details()

                elif choice == '4':
                    print("Thank you for using Bank Manager")
                    break

            except ValueError:
                print("Invalid amount. Please enter a number.")
        else:
            print("Invalid choice. Please choose from 1, 2, 3 or 4.")

def start():
    print("Welcome To The Bank Account Manager.\n"
        "Do you have an account?\n")
    print("1.Sign in \n2.Sign up\n")

    while True:
        welcome = input("Choose an option: ")
        if welcome == "1":
            sign_in()
            break

        elif welcome == "2":
            create_account()
            break

        else:
            print("invalid option, Enter the given the option.")

if __name__ == '__main__':
    start()






   