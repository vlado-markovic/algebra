# TODO: Napraviti tk app za prikaz i zapis passworda.
# TODO: App mora imati 3 ekrana. Main screen, deails screen, add new screen. 
# TODO: MAIN SCREEN; mora imati listu zapisa i gump za dodati novi zapis. 
# TODO: klik na svaki od zapisa treba voditi na detalje zapisa
# TODO: klik na gumb za dodavanje zapisa vodi na odvojeni ekran
# TODO: DETAILS SCREEN; prikazuje sve datalje oko zapisa
# TODO: ADD NEW SCREEN; prihvaca unose korisnika te na klik gumba iz sprema
# TODO: ZAPIS ima: ime, username, password, link, opis

import tkinter as tk
from tkinter import messagebox, scrolledtext
import tkinter.ttk as ttk
import pyperclip

class App:
    def __init__(self) -> None:
        self.logs = {}
        
        # dohvatit bazu i popunit self.logs s vrijednostima iz iste
        
        
        self.root = tk.Tk()
        self.root.title("Password manager")

        # Main
        
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack()
        
        self.pass_listbox = tk.Listbox(self.main_frame, width=50)
        self.pass_listbox.pack(side=tk.LEFT, padx=10, pady=10)
        self.pass_listbox.bind('<<ListBoxSelect>>', self.show_details)
        
        self.add_button = tk.Button(
            self.main_frame, 
            text='Add new', 
            command=self.show_input_screen)

        self.add_button.pack(padx=5, pady=10)

        # Password add/input screen

        self.input_screen = tk.Toplevel(self.root) #- instanca roota - i mjenja screen
        self.input_screen.title = ('Add new password')
        self.input_screen.withdraw() # po defaultu je skriven
       
        self.name_entry = self.pm_input_field(self.input_screen, "Ime")
        self.username_entry = self.pm_input_field(self.input_screen, "Korisnicko Ime")
        self.password_entry = self.pm_input_field(self.input_screen, "Password", show='*')
        self.link_entry = self.pm_input_field(self.input_screen, "Link")
        self.desc_entry = self.pm_input_box(self.input_screen, "Opis")

        self.submit_button =tk.Button(self.input_screen, text="Predaj", command=self.add_password_entry)
        self.submit_button.pack(padx=10, pady=10)

        #DETAILS SCREEN
        self.details_screen = tk.Toplevel(self.root)
        self.details_screen.title('Detalji')
        self.details_screen.withdraw() # Sakri detalje na pocetku

        self.details_frame = tk.Frame(self.details_screen)
        self.details_frame.pack(padx=10, pady=10)

        self.details_labels = {}
        self.copy_buttons = {}

        fields = ['Name', 'Username', "Password", "Link", "Description"]
        row = 0
        for field in fields:
            label = ttk.Label(self.details_frame, text= field + ":")
            label.grid(row=row, column= 0, sticky='W', padx= 0, pady= 5)
            self.details_labels[field] = ttk.Label(self.details_frame, text='')
            self.details_labels[field].grid(row= row, column= 1, sticky='W', padx=0, pady=5)

            if field in ['Username', 'Password', 'Link']:
                copy_button = ttk.Button(
                    self.details_frame, 
                    text='Copy', 
                    command=lambda f= field: self.copy_to_clipboard(f) #lambda je anonimna funcija
                    # anonimna funkcija znaci da nije definirana s defom i nema ime
                    # ovdije je iskoristeno da smo napravili anonimnu funkiju koja prima parametar f 
                    # da bi mogli pozvati imenovnu funkciju copy(f) s tim parametrom
                )
                copy_button.grid(row= row, column= 2, padx= 5, pady= 5)
                self.copy_buttons[field] = copy_button

            row += 1
    # def foo(self, f):
    #     self.copy_to_clipboard(f)

        self.back_button = tk.Button(
            self.details_screen, 
            text='Nazad', 
            command=self.back_to_main
        )
        self.back_button.pack(padx=10, pady=10)



        
    def pm_input_field(self, parent, label_text, show=None):
        
        frame = tk.Frame(parent)
        frame.pack(padx=10, pady=10, fill=tk.X)
        
        label = tk.Label(frame, text=label_text, width=20)
        label.pack(side=tk.LEFT)
        
        entry = tk.Entry(frame)
        entry.pack(
            side=tk.LEFT,
            padx=5,
            pady=0,
            expand=True,
            fill=tk.X
        )
        return entry
    
    def pm_input_box(self, parent, label_text, show=None):
        
        frame = tk.Frame(parent)
        frame.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        label = tk.Label(frame, text=label_text, width=20)
        label.pack(side=tk.LEFT)

        entry = scrolledtext.ScrolledText(
            frame, 
            height=4, 
            width=50, 
            wrap=tk.WORD,
            show=show
        )
        entry.pack(
            side=tk.LEFT, 
            padx=5, 
            pady=0, 
            expand=True, 
            fill=tk.BOTH
        )

        return entry 


    def add_password_entry(self):
        name =  self.name_entry.get().strip()
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        link = self.link_entry.get().strip()
        desc = self.desc_entry.get('1.0', tk.END).strip()


        # ovo bi se obavljalo u servisnom sloju
        if name:
            self.logs[name] = {
                'Username': username,
                'Password': password,
                'Link': link,
                'Descrpiton': desc
            }

            messagebox.showinfo('Uspijeh', 'Password je dodan uspjesno!')

            self.name_entry.delete(0, tk.END)
            self.username_entry.delete(0, tk.END)
            self.password_entry.delete(0, tk.END)
            self.link_entry.delete(0, tk.END)
            self.desc_entry.delete("1.0", tk.END)

            self.input_screen.withdraw() # sakri input
            self.root.deiconify() # pokazi main screen
            self.update_pass_listbox()
        
        else:
            messagebox.showerror("ERROR", "Mora postojati ime zapisa!")

    def update_pass_listbox(self):
        self.pass_listbox.delete(0, tk.END)
        for name in self.logs:
            self.pass_listbox.insert(tk.END, name)

    def show_details(self, event):
        selection = self.pass_listbox.curselection() # doynajemo koji element je odabran
        if selection:
            pass_name = self.pass_listbox.get(selection[0])
            entry = self.logs[pass_name]

            for field, label in self.details_labels.items():
                if field in entry:
                    label.config(text=entry[field])
                else:
                    label.config(text='')

            self.details_screen.deiconify() # priakzi datelje
            self.root.withdraw() # sakri main

    def show_input_screen(self):
        self.input_screen.deiconify() # Prizaki ekran input screen
        self.root.withdraw() # Sakri root ekran (main)


    def back_to_main(self):
        self.details_screen.withdraw()
        self.root.deiconify()

    def copy_to_clipboard(self, field):
        selection = self.pass_listbox.curselection() # doynajemo koji element je odabran
        if selection:
            pass_name = self.pass_listbox.get(selection[0])
            entry = self.logs[pass_name]
            if field in entry:
                pyperclip.copy(entry[field])
                messagebox.showinfo('Kopiran', f'Virjednost {field} je kopirana!')
            else:
                messagebox.showwarning("Warning", f'Ne postojeca vrijednost {field}!')


    def show_details(self):
        pass
    
    def show_input_screen(self):
        self.input_screen.deiconify()
        self.root.withdraw()
        
        
    def run(self):
        self.root.mainloop()
        
if __name__=="__main__":
    app = App()
    app.run()