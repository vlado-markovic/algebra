from tkinter import *


class Login(Tk):
    
    def __init__(self):
        super().__init__()
         
        self.login_label = Label(self, text="Prijava")
        self.login_label.pack()
        
        self.user_name_label = Label(self, text="Korisnicko Ime")
        self.user_name_label.pack()
        
        self.user_name = Entry(self, width=40, borderwidth=5)
        self.user_name.insert(0, "unesite vase korisnicko ime")
        self.user_name.pack()
        
        self.password_label = Label(self, text="Lozinka")
        self.password_label.pack()
        
        self.password = Entry(self, text="Unesite svoju lozinku", width=40, borderwidth=5)
        self.password.insert(0, "unesite vasu lozinku")
        self.password.pack()
          
        
        def log_in ():
            name = self.user_name.get()
            passw = self.password.get()
            
            print (name, passw)


        self.login_button = Button(self, text="Prijavi me", command=log_in)
        self.login_button.pack()


login = Login()
login.title("Welcome to PyFlora")
login.mainloop()
