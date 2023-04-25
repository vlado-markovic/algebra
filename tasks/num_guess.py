import random

def mode1():
    secret_number = random.randint(1, 100)
    print("I am thinking of a number between 1 and 100. Try to guess it!")
    while True:
        try:
            guess = int(input("Your guess: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if guess == secret_number:
            print("Congratulations! You guessed the number.")
            break
        elif guess < secret_number:
            print("The number I am thinking of is higher.")
        else:
            print("The number I am thinking of is lower.")

def mode2():
    print("Think of a number between 1 and 100. I will try to guess it!")
    low = 1
    high = 100
    while True:
        guess = random.randint(low, high)
        print("Is the number", guess, "?")
        answer = input("Enter 'h' if the number is higher, 'l' if the number is lower, or 'c' if I guessed correctly: ")
        if answer == 'c':
            print("I win! Thanks for playing.")
            break
        elif answer == 'h':
            low = guess + 1
        elif answer == 'l':
            high = guess - 1
        else:
            print("Invalid input. Please enter 'h', 'l', or 'c'.")

def show_rules():
    print("Welcome to Guess the Number!")
    print("In mode 1, the computer thinks of a number and you try to guess it.")
    print("In mode 2, you think of a number and the computer tries to guess it.")
    print("At the end of each guess, the program will tell you if the number is higher or lower than your guess.")
    print("To quit the game, choose the option to exit.")

def main():
    while True:
        print("Please select an option:")
        print("1. Play mode 1: guess the computer's number")
        print("2. Play mode 2: let the computer guess your number")
        print("3. Show rules")
        print("4. Quit")
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == 1:
            mode1()
        elif choice == 2:
            mode2()
        elif choice == 3:
            show_rules()
        elif choice == 4:
            print("Thanks for playing!")
            break
        else:
            print("Invalid input. Please choose a valid option.")

if __name__ == "__main__":
    main()
