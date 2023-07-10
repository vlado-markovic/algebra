from tkinter.ttk import (
    Frame,
    Label,
    Entry,
    Button,
    Labelframe
)

class PinFrame(Frame):
    def __init__(self, master, check_fn) -> None:
        super().__init__(master)
        
        # Initial setup
        Label(self, text="Pin Panel").grid(row=0, column=0, sticky="nsew")
        self.keypad = Frame(self, relief="ridge")
        self.feedback = Labelframe(self, text="Info")
        self.feedback_label = Label(self.feedback)
        self.feedback_label.grid(row=0, column=0, sticky="nsew", pady=5)
        self.keypad.grid(row=1, column=0, sticky="nsew", pady=5)
        self.feedback.grid(row=2, column=0, sticky="nsew", pady=5)
        self.feedback.columnconfigure(0, weight=1)
        self.feedback.rowconfigure(0, weight=1)
        self.back = Button(self, text="Back")
        self.back.grid(row=3, column=0, sticky="e", pady=5)
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)

        self.keypad.columnconfigure(0, weight=1)
        self.keypad.columnconfigure(1, weight=1)
        self.keypad.columnconfigure(2, weight=1)
        self.keypad.rowconfigure(0, weight=1)
        self.keypad.rowconfigure(1, weight=1)
        self.keypad.rowconfigure(2, weight=1)
        self.keypad.rowconfigure(3, weight=1)
        self.keypad.rowconfigure(4, weight=1)
        self.check_fn = check_fn
        
        # Keyboard
        self.pin = Entry(self.keypad, show="*", state="disabled")
        self.pin.grid(row=0, column=0, columnspan=3,padx=5, pady=5, sticky="ew")
        
        self.pin.bind('<Enter>', self.enter)
        self.pin.bind('<Leave>', self.leave)

        Button(self.keypad, text="1", command=lambda:self.modify(1)).grid(row=1, column=0, padx=5, pady=5)
        Button(self.keypad, text="2", command=lambda:self.modify(2)).grid(row=1, column=1, padx=5, pady=5)
        Button(self.keypad, text="3", command=lambda:self.modify(3)).grid(row=1, column=2, padx=5, pady=5)
        
        Button(self.keypad, text="4", command=lambda:self.modify(4)).grid(row=2, column=0, padx=5, pady=5)
        Button(self.keypad, text="5", command=lambda:self.modify(5)).grid(row=2, column=1, padx=5, pady=5)
        Button(self.keypad, text="6", command=lambda:self.modify(6)).grid(row=2, column=2, padx=5, pady=5)

        Button(self.keypad, text="7", command=lambda:self.modify(7)).grid(row=3, column=0, padx=5, pady=5)
        Button(self.keypad, text="8", command=lambda:self.modify(8)).grid(row=3, column=1, padx=5, pady=5)
        Button(self.keypad, text="9", command=lambda:self.modify(9)).grid(row=3, column=2, padx=5, pady=5)


        Button(self.keypad, text="0", command=lambda:self.modify(0)).grid(row=4, column=1, padx=5, pady=5)

        Button(self.keypad, text="C", command=self.clear).grid(row=4, column=2)

    def modify(self, value):
        self.pin.config(state="normal")
        self.pin.insert("end", value)
        self.pin.config(state="disabled")
        self.check()

    def clear(self):
        self.pin.config(state="normal")
        value = self.pin.get()
        self.pin.delete(0, "end")
        self.pin.insert(0, value[0:-1])
        self.pin.config(state="disabled")

    def enter(self, event):
        self.pin.config(state="normal",show="")

    def leave(self, event):
        self.pin.config(state="disabled",show="*")

    def check(self):
        value = self.pin.get()
        if len(value)==4:
            self.pin.config(state="normal")
            self.pin.delete(0, "end")
            self.pin.config(state="disabled")
            self.check_fn(value)
