import os
import datetime

# Dictionary to store account information
accounts = {}

# Generate account number
def generate_account_number():
    global accounts
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month).zfill(2)
    num = str(len(accounts) + 1).zfill(5)
    return f"BA-{year}-{month}-{num}"

# Create a new account
def create_account():
    global accounts
    name = input("Enter company name: ")
    street = input("Enter street and number: ")
    postal_code = input("Enter postal code: ")
    city = input("Enter city: ")
    while True:
        oib = input("Enter OIB (11 digits): ")
        if len(oib) == 11:
            break
    responsible_person = input("Enter responsible person name: ")
    currency = input("Enter currency (EUR or HRK): ")
    initial_balance = float(input("Enter initial balance: "))
    account_number = generate_account_number()
    account = {
        "name": name,
        "street": street,
        "postal_code": postal_code,
        "city": city,
        "oib": oib,
        "responsible_person": responsible_person,
        "currency": currency,
        "balance": initial_balance
    }
    accounts[account_number] = account
    print(f"Account created with account number {account_number}")

# Display account balance
def display_balance():
    global accounts
    account_number = input("Enter account number: ")
    if account_number in accounts:
        account = accounts[account_number]
        print(f"Account balance: {account['balance']} {account['currency']}")
    else:
        print("Invalid account number")

# Display account transactions
def display_transactions():
    global accounts
    account_number = input("Enter account number: ")
    if account_number in accounts:
        account = accounts[account_number]
        print(f"Transactions for account number {account_number}:")
        # Here you would display the transactions for the account
    else:
        print("Invalid account number")

# Deposit money into account
def deposit_money():
    global accounts
    account_number = input("Enter account number: ")
    if account_number in accounts:
        amount = float(input("Enter amount to deposit: "))
        account = accounts[account_number]
        account['balance'] += amount
        print(f"{amount} {account['currency']} deposited into account {account_number}")
    else:
        print("Invalid account number")

# Withdraw money from account
def withdraw_money():
    global accounts
    account_number = input("Enter account number: ")
    if account_number in accounts:
        amount = float(input("Enter amount to withdraw: "))
        account = accounts[account_number]
        if account['balance'] >= amount:
            account['balance'] -= amount
            print(f"{amount} {account['currency']} withdrawn from account {account_number}")
        else:
            print("Insufficient funds")
    else:
        print("Invalid account number")

# Main menu
while True:
    # display main menu options
    print("Main menu:")
    print("1. Create company account")
    print("2. View account balance")
    print("3. View account transactions")
    print("4. Deposit money")
    print("5. Withdraw money")
    print("6. Exit")
    
    # get user input
    choice = input("Enter your choice: ")
    
    # handle user choice
    if choice == "1":
        create_account()
    elif choice == "2":
        display_balance()
    elif choice == "3":
        display_transactions()
    elif choice == "4":
        deposit_money()
    elif choice == "5":
        withdraw_money()
    elif choice == "6":
        # exit the program
        break
    else:
        print("Invalid choice. Please try again.")
    
    # clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')
 