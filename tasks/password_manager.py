#? Napraviti program koji zapsuje username i password korisnika
#? Postoje 2 razine prava: ADMIN i obicni user
#? 1 admin je unaprijed upisan "hardcodiran"
#? 1. osoba unosi username i password
#? Ispisuje se pozdravna poruka i meni, ili poruku o gresci (ako nisu dobri username i password)

####? Admin meni: 
#? 1. DODAJ korisnika -> admin unosi username i password i je li user admin
#? 2. PRIKAZI sve korisnike -> ispisuju se username-ovi svih korisnika
#? 3. PROMIJENI svoj password -> admin unosi stari pass i novi, a u bazi se editira
#? 4. OBRISI korisnika -> admin unosi username a korisnik s tim username-om se obrise
#? 5. LOGOUT -> vrati se nazad na login
#? 6. EXIT -> zagasi program

####? User meni:
#? 1. PROMIJENI password -> unosi stari i novi password
#? 2. LOGOUT -> vrati se an login

# ! HELP
# ! Treba vam lista admina
# ! Treba vam dict usere (username je key, a password value)
# ! Admin se dodaje u oba obijekta, ostali user samo u dict
# ! Admini se brisu iz oba obijekta, a useri samo iz dict-a
# ! Za login uporedba username-a i passworda iz dict-a
# ! Za promijenu passworda treba usporedit stari pass i ono sto ej u dict-u, ako odgovoara update-at
# ! Treba vam jedna varijabla koja pamti trenutno ulogiranog usera

users = {"admin": 'admin'}

admins = set()
admins.add("admin")

def add_user():
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    users[username] = password
    is_admin = input("Is this user an admin? (y/n): ")
    if is_admin.casefold() == 'y':
        admins.add(username)
        print("User added as admin successfully.")
    else:
        print("User added successfully.")

    
def show_all_users():
    print("List of all users:")
    for username, password in users.items():
        print(username)
        
def change_password(username):
    if username not in users:
        print("Username not found.")
        return

    old_password = input("Enter your old password: ")
    if users[username] != old_password:
        print("Old password incorrect. Password change aborted.")
        return

    while True:
        new_password = input("Enter your new password: ")
        password_confirm = input("Confirm your new password: ")

        if new_password != password_confirm:
            print("Passwords do not match. Please try again.")
            continue

        users[username] = new_password
        print("Password updated successfully.")
        break
        
def delete_user():
    username = input("Enter the username to delete: ")
    if username in users:
        del users[username]
        if username in admins:
            admins.remove(username)
        print("User deleted successfully.")
    else:
        print("User not found.")
        
def logout():
    print("You have been logged out.")

def admin_menu(current_user):
    while True:
        print("Select an option:")
        print("1. Add user")
        print("2. Show all users")
        print("3. Change password")
        print("4. Delete user")
        print("5. Logout")
        print("6. EXIT")

        choice = input("Enter your choice (1-6): ")

        if choice not in range(1, 7):
            print("Invalid choice. Please enter a number from 1 to 6.")
            continue

        if choice == '1':
            add_user()
        elif choice == '2':
            show_all_users()
        elif choice == '3':
            change_password(current_user)
        elif choice == '4':
            delete_user()
        elif choice == '5':
            logout()
            break
        else:
            exit()

def user_menu(current_user):
    while True:
        print("Select an option:")
        print("1. Change password")
        print("2. Logout")

        choice = input("Enter your choice: ")

        if choice not in range(1, 3):
            print("Invalid choice. Please enter 1 or 2.")
            continue

        if choice == '1':
            change_password(current_user)
        else:
            logout()
            break

def login():
    global current_user  # Access the global variable

    while True:
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        if username not in users or users[username] != password:
            print("Invalid username or password. Please try again.")
            continue

        print("Login successful.")
        current_user = username  # Set the global variable to the logged-in user's username
        if username in admins:
            admin_menu(current_user)
        else:
            user_menu(current_user)
        break

def main():
    while True:
        login()

if __name__ == "__main__":
    main()

