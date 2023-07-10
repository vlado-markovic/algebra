from tkinter.ttk import (Frame, Label, Entry, Button, Labelframe, Treeview, Checkbutton)
from tkinter import NO, BooleanVar


class AdminFrame(Frame):
    def __init__(self, master) -> None:
        super().__init__(master)
        self._id = None
        self.checkbox_state = BooleanVar()
        self.users_frame = Labelframe(self, text="Users List")
        self.users_frame.grid(row=0, column=0, sticky="nsew")
        self.user_frame = Frame(self)

        self.users_treeview = Treeview(self.users_frame)
        self.users_treeview["columns"] = ("Name", "Surname")

        self.users_treeview.column("#0", width=0, stretch=NO)
        self.users_treeview.column("Name", width=100, minwidth=100)
        self.users_treeview.column("Surname", width=100, minwidth=100)
        self.users_treeview.heading("#0", text="ID")
        self.users_treeview.heading("Name", text="Name")
        self.users_treeview.heading("Surname", text="Surname")

        self.users_treeview.grid(row=0, column=0, sticky="nsew")
        self.users_frame.columnconfigure(0, weight=1)
        self.users_frame.rowconfigure(0, weight=1)

        Label(self.user_frame, text="Name").grid(row=0, column=0, sticky="e", padx=5)
        Label(self.user_frame, text="Surname").grid(row=1, column=0, sticky="e", padx=5)
        Label(self.user_frame, text="PIN (4 characters)").grid(row=2, column=0, sticky="e", padx=5)
        Label(self.user_frame, text="Active").grid(row=3, column=0, sticky="e", padx=5)

        self.first_name = Entry(self.user_frame)
        self.first_name.grid(row=0, column=1, sticky="we", padx=5)
        self.last_name = Entry(self.user_frame)
        self.last_name.grid(row=1, column=1, sticky="we", padx=5)
        self.password = Entry(self.user_frame)
        self.password.grid(row=2, column=1, sticky="we", padx=5)
        self.active = Checkbutton(self.user_frame, variable=self.checkbox_state)
        self.active.grid(row=3, column=1, sticky="we", padx=5)
        
        self.actions_frame = Frame(self.user_frame)
        self.add_btn = Button(self.actions_frame, text="Save")
        self.cls_btn = Button(self.actions_frame, text="Discard")
        self.del_btn = Button(self.actions_frame, text="Delete")
        self.back = Button(self, text="Back")
        self.back.grid(row=1, column=1, sticky="e")
        self.add_btn.grid(row=0, column=0)
        self.cls_btn.grid(row=0, column=1)
        self.del_btn.grid(row=0, column=2)
        self.actions_frame.grid(row=4, column=0, columnspan=2)

        self.user_frame.columnconfigure(0,weight=1)
        self.user_frame.columnconfigure(1,weight=1)
        self.user_frame.rowconfigure(0,weight=1)
        self.user_frame.rowconfigure(1,weight=1)
        self.user_frame.rowconfigure(2,weight=1)
        self.user_frame.rowconfigure(3,weight=1)
        self.user_frame.rowconfigure(4,weight=1)
        self.user_frame.grid(row=0, column=1, sticky="nsew")

        self.columnconfigure(1,weight=1)
