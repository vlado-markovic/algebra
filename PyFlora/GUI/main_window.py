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

# default coordinates of main screen 
def center_window(window_instance, width=1000, height=500):
    # get screen width and height
    screen_width = window_instance.winfo_screenwidth()
    screen_height = window_instance.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width / 2) - (window_width / 2)
    y = (screen_height / 2) - (window_height / 2)
    
    
    norm_width = x #(screen_width - width)
    norm_height = y #(screen_height - height)
    
    
    print ('%dx%d+%d+%d' % (norm_width, norm_height, x, y))

    return ('%dx%d+%d+%d' % (norm_width, norm_height, x, y))
    #return ('%dx%d+%d+%d' % (x, y))