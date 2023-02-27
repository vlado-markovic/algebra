import tkinter as tk

class GUIWindow(tk.Tk):
    def __init__(self):
        super().__init__()
        
        # Create label to display data
        self.data_label = tk.Label(self, text="Hello World!")
        self.data_label.pack()
        
        # Create button to update data
        self.update_button = tk.Button(self, text="Update", command=self.update_data)
        self.update_button.pack()
        
    def update_data(self):
        # Update label with new data
        self.data_label.configure(text="New data!")
        
# Create GUI window
gui = GUIWindow()
gui.mainloop()
