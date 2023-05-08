import os
import sys
import datetime
import time
import re

# Dictionary to store account information
accounts = {}

# Generate account number
def generate_account_number(): 
    year = str(datetime.datetime.now().year)
    month = str(datetime.datetime.now().month).zfill(2)
    num = str(len(accounts) + 1).zfill(5)
    return f"BA-{year}-{month}-{num}" # --> "BA-YEAR-MONTH-NNNNN"

# Only 11 character are allowed for Croatian citizen personal num
def validate_oib(oib):
    pattern = r'^[0-9]+$'  # Matches one or more digits from start to end
    
    if re.match(pattern, oib):
        return True
    else:
        return False

# Create a new account
def create_account():
    name = input("Enter company name: ")
    street = input("Enter street and number: ")
    postal_code = input("Enter postal code: ")
    city = input("Enter city: ")
    
    while True:
        oib = input("Enter OIB (11 digits): ")
        if len(oib) == 11 and validate_oib(oib):
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
        "balance": initial_balance,
        "transactions": []
    }
    
    accounts[account_number] = account
    print(f"Account created with account number {account_number}")
    
    time.sleep(2)

# get the account number from user input, and validate it
def get_account_number():
    while True: 
        try:
            account_number = input("Enter account number: ")
            if account_number in accounts:
                return account_number
            else:
                print("Invalid account number")
        except Exception as e:
            print("An error occurred:", str(e))

# Display account balance
def display_balance(account):  
    print(f"Account balance: {accounts[account]['balance']} {accounts[account]['currency']}")
    time.sleep(4)

# Display account transactions
def display_transactions(account):
    trasactions = accounts[account]["transactions"]
    print(f"Transactions for account number {trasactions}: ")
    time.sleep(4)

# Log the withdraw or deposit actions   
def log_transaction(type, acc_num, amount):
    accounts[acc_num]['transactions'].append(f"{type} {amount}")

def deposit(acc_num, amount):
    accounts[acc_num]['balance'] += amount
    log_transaction("deposited: ", acc_num, amount)
    
# Deposit money into account
def deposit_money(acc_num):
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        deposit(acc_num, amount)
        print(f"{amount} {accounts[acc_num]['currency']} deposited into account {acc_num}")
        time.sleep(1)
    else: 
        print ("Inesert amount bigger than zero!")
        time.sleep(1)
            
def withdraw(acc_num, amount):       
    if accounts[acc_num]['balance'] >= amount:
       accounts[acc_num]['balance'] -= amount
       log_transaction("withdrawn", acc_num, amount)
    else:
        print("Insufficient funds")
    
# Withdraw money from account
def withdraw_money(acc_num):
    amount = float(input("Enter amount to withdraw: "))
    if amount > 0:
        withdraw(acc_num, amount)
        print(f"{amount} {accounts[acc_num]['currency']} withdrawn from account {acc_num}")
        time.sleep(1)
    else:
        print("Inesert amount bigger than zero!")
        time.sleep(1)
        
# execute the user option from menu    
def start_options(choice):
    if choice == "1":
        create_account()
    elif choice == "2":
        display_balance(get_account_number())
    elif choice == "3":
        display_transactions(get_account_number())
    elif choice == "4":
        deposit_money(get_account_number())
    elif choice == "5":
        withdraw_money(get_account_number())
    elif choice == "6":
        # exit the program
        sys.exit()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1)
        
# display main menu options
def show_menu():
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
    start_options(choice)    

# clear content in terminal
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def start_screen():
    show_menu()
 
    # clear the screen
    clear_screen()
    
    # debugging mode :) 
    print (accounts)

# show the main menu
while True:
    start_screen()