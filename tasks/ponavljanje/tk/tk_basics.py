import tkinter as tk


# root = tk.Tk()
# root.title('GUI')

# root.geometry('800x800')

# button = tk.Button(root, text='Klikni gumbbbb')
# button.pack()
# tk.Label()
# tk.PhotoImage()
# tk.Entry()
# tk.Checkbutton()
# tk.Radiobutton()
# tk.Listbox()
# tk.Menu()
# tk.Menubutton()
# tk.Message()

# root.mainloop() # pokreni prikaz



# geometrije

# button.pack() --> postavlja elemente jedan ispod drugog
# button.place(x=100, y=50) --> precizan u pixel, ali trebaju mu x i y koordinate, tesko za slagati
# button.grid(row=1, column=0)  --> najcesce koristen, mix predhodna dva, daje slozenije sucelje (mrezu), bez proslijedivanja tocnih koordinata


# Eventi

# odaberemo event iz liste 

# <Button-1>  --> mouse button lijevi
# <ButtonRelease-1>
# <Enter>
# <FocusIn>
# <Return>
# a --> za slovo a
# <Key> --> bilo sto ako se pritisne


def handle_key(event): # mora primati event koji ju je pozvao
    label_var.set(event.char)
    
    pass

root = tk.Tk()
root.title('GUI')

root.geometry('800x800')

label_var = tk.StringVar()
label_var.set('label')

label = tk.Label(root, textvariable=label_var)
label.pack()

root.bind('<Key>', handle_key) # --> bind spaja event i funkciju (callback)
root.mainloop()