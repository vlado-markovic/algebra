from tkinter import *


root = Tk()
root.title("headline")

# root.iconbitmap('PyFlora/GUI/media/82_85230.ico')

my_label_1 = Label(root, text="hello world !!")
my_label_2 = Label(root, text="some some !!")

my_label_1.grid(row=0, column=0)
my_label_2.grid(row=1, column=1)

my_button = Button(root, text="click me")
my_button.grid()

my_button_2 = Button(root, text="click me 22", state="disabled", padx=22, pady = 12)
my_button_2.grid()


def myClick():
    my_label = Label(root, text="clicked it ")
    my_label.grid()
    
my_button_3 = Button(root, text="neki text", command = myClick, fg="blue", bg="white")
my_button_3.grid()


e = Entry(root, text="Enter your username", width=50)
e.grid()


root.mainloop()









# class GUIWindow(tk.Tk):
#     def __init__(self):
#         super().__init__()
        
#         # Create label to display data
#         self.data_label = tk.Label(self, text="Hello World!")
#         self.data_label.pack()
        
#         # Create button to update data
#         self.update_button = tk.Button(self, text="Update", command=self.update_data)
#         self.update_button.pack()
        
#     def update_data(self):
#         # Update label with new data
#         self.data_label.configure(text="New data!")
        
# # Create GUI window
# #gui = GUIWindow()
# #gui.mainloop()

# # default coordinates of main screen 
# def center_window(window_instance, width=1000, height=500):
#     # get screen width and height
#     screen_width = window_instance.winfo_screenwidth()
#     screen_height = window_instance.winfo_screenheight()

#     # calculate position x and y coordinates
#     x = (screen_width / 2) - (window_width / 2)
#     y = (screen_height / 2) - (window_height / 2)
    
    
#     norm_width = x #(screen_width - width)
#     norm_height = y #(screen_height - height)
    
    
#     print ('%dx%d+%d+%d' % (norm_width, norm_height, x, y))

#     return ('%dx%d+%d+%d' % (norm_width, norm_height, x, y))
#     #return ('%dx%d+%d+%d' % (x, y))