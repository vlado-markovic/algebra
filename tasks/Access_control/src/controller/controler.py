from tkinter.messagebox import (
    showerror,
    showinfo,
    askokcancel
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.ent.database import DBContext

from src.view.main_panel import MainFrame
from src.view.pin_panel import PinFrame
from src.view.admin_panel import AdminFrame
from src.service.user_orm import (
    insert_user,
    update_user,
    delete_user,
    get_items,
    get_by_id
)

class MainController:
    def __init__(self, tk, db: "DBContext"):
        self.tk = tk
        self.db = db
        self.current_frame = MainFrame(self.tk) 
        self.current_frame.open.configure(command=self.open)
        self.current_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.tk.columnconfigure(0, weight=1)
        self.tk.rowconfigure(0, weight=1)


    def main_frame(self):
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = MainFrame(self.tk) 
        self.current_frame.open.configure(command=self.open)
        self.current_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.tk.columnconfigure(0, weight=1)
        self.tk.rowconfigure(0, weight=1)


    def open(self):
        if isinstance(self.current_frame, MainFrame):
            self.current_frame.destroy()
        self.current_frame = PinFrame(self.tk, self.check_fn)
        self.current_frame.back.configure(command=self.main_frame)
        self.current_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.tk.columnconfigure(0, weight=1)
        self.tk.rowconfigure(0, weight=1)


    def check_fn(self, value:str):
    
        result = self.db.login(value)
      
        if result is None:
            self.current_frame.feedback_label.configure(text=f"Wrong password, please try again")
        elif result.system:
            if askokcancel(title="Admin acess", message="Do you want to continue as Admin?"):
                self.admin_screen()
        elif result.active: 
            self.current_frame
            self.current_frame.feedback_label.configure(text=f"Hi {result.first_name}, welcome, access granted !")
        elif not result.active:
            self.current_frame
            self.current_frame.feedback_label.configure(text=f"Hi {result.first_name} your membership expired")

   
    def admin_screen(self):
        if isinstance(self.current_frame, PinFrame):
            self.current_frame.destroy()
      
        self.current_frame = AdminFrame(self.tk)
        self.current_frame.cls_btn.configure(command=self.clear_all)
        self.current_frame.add_btn.configure(command=self.on_save)
        self.current_frame.del_btn.configure(command=self.on_delete)
        self.current_frame.users_treeview.bind("<<TreeviewSelect>>", self.get_selected_row)
        self.current_frame.back.configure(command=self.main_frame)
        for user in get_items(self.db):
            self.current_frame.users_treeview.insert("", "end", text=str(user.id), values=(user.first_name, user.last_name))
        self.current_frame.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.tk.columnconfigure(0, weight=1)
        self.tk.rowconfigure(0, weight=1)

    def clear_all(self):
        self.current_frame.first_name.delete(0, "end") 
        self.current_frame.last_name.delete(0, "end") 
        self.current_frame.password.delete(0, "end") 
        self.current_frame.checkbox_state.set(False) 
        self.current_frame._id=None

    def on_save(self):
        first_name= self.current_frame.first_name.get() 
        last_name= self.current_frame.last_name.get() 
        password= self.current_frame.password.get()
        checkbox_state= self.current_frame.checkbox_state.get()
        
        if 0 < len(first_name) <=50 and 0 < len(last_name) <=50:
            if len (password) == 4 and password.isdigit():
                if self.current_frame._id is not None:
                    update_user(self.db, id=self.current_frame._id, first_name=first_name, last_name=last_name, password=password, active=checkbox_state) 
                    
                    showinfo("Notification", "User edited")
                else:
                    user = insert_user(self.db,first_name=first_name, last_name=last_name, password=password, active=checkbox_state)
                    
                    if not user:
                        showerror("Error", "Password allready in use")
                    else:
                        self.current_frame.users_treeview.insert("", "end", text=str(user.id), values=(user.first_name, user.last_name)) # type: ignore
                        showinfo("Notification", "User added")
            else:
                showerror("Warning", "PIN must have 4 numbers and no charachters allowed")
        else:
            showerror("Warning", "Name and Last name must have max 50 characters")


    def on_delete(self):
        if self.current_frame._id is not None:
            delete_user(self.db, self.current_frame._id)
            self.clear_all()
            self.current_frame.users_treeview.delete(*self.current_frame.users_treeview.selection())


    def get_selected_row(self, event):

        selected_item = self.current_frame.users_treeview.focus()
        value = self.current_frame.users_treeview.item(selected_item, 'text')  
        usr = get_by_id(self.db, value)
        
        self.current_frame.first_name.delete(0, "end")
        self.current_frame.last_name.delete(0, "end") 
        self.current_frame.password.delete(0, "end") 
        self.current_frame.checkbox_state.set(False) 
        self.current_frame.first_name.insert(0, usr.first_name)
        self.current_frame.last_name.insert(0, usr.last_name) 
        self.current_frame.password.insert(0, usr.password) 
        self.current_frame.checkbox_state.set(usr.active) 
        self.current_frame._id=usr.id 