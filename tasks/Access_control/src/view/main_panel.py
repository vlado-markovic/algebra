from pathlib import Path 
from tkinter.ttk import (Frame, Label, Button)
from tkinter import Toplevel

class MainFrame(Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        Label(self, text="Access Control").grid(row=0, column=0, columnspan=2)
        self.ring = Button(self, text="Ring", command=self.wait_for_person)
        self.open = Button(self, text="Unlock")
        self.ring.grid(row=1, column=0, sticky="w")
        self.open.grid(row=1, column=1, sticky="e")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
  
    def wait_for_person(self):
        tplvl = Toplevel(self.master)
        tplvl.title("Notification")
        x = (self.master.winfo_screenwidth() - self.winfo_reqwidth()) / 2
        y = (self.master.winfo_screenheight() - self.winfo_reqheight()) / 2
        tplvl.geometry(f"+{int(x)}+{int(y)}")
        Label(tplvl, text="Please wait until someone opens the door for you").grid(row=0, column=0, padx=15, pady=15, ipadx=15, ipady=15, sticky="nsew")
        Button(tplvl,text="Ok", command=tplvl.destroy).grid(row=1, column=0, padx=15, pady=15, ipadx=15, ipady=15, sticky="nsew")
        tplvl.resizable(False,False)
        tplvl.attributes("-topmost", True) 
        tplvl.attributes("-toolwindow", 1)
        tplvl.grab_set()
        tplvl.wait_window()
