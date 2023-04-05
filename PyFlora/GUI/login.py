import tkinter as tk
# from main_window import center_window
 
# from users.login import correct_username, correct_password

class LoginScreen(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create username and password labels and entries
        self.username_label = tk.Label(self, text="Username:")
        self.username_entry = tk.Entry(self)
        self.password_label = tk.Label(self, text="Password:")
        self.password_entry = tk.Entry(self, show="*")

        # Create login button
        self.login_button = tk.Button(self, text="Login", command=self.login)

        # Position the widgets using the grid layout manager
        self.username_label.grid(row=2500, column=2500)
        self.username_entry.grid(row=2500, column=2501)
        self.password_label.grid(row=2501, column=2500)
        self.password_entry.grid(row=2501, column=2501)
        self.login_button.grid(row=2, column=1)

    def login(self):
        # Get the entered username and password
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username and password are correct
        if username == "admin" and password == "password":
            print("Login successful")
            # go to the main page
            
        else:
            # loop 3 times
            print("Login failed")





# Create the login screen
login_screen = LoginScreen()
login_screen.geometry("2000x1200+2000+150") # (use center_window function - if not manually specified)
login_screen.title("PyFlora Login")
login_screen.config(bg="#90EE90")


# Run the event loop
login_screen.mainloop()
