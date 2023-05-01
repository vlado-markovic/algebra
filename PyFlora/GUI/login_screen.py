import tkinter as tk

root = tk.Tk()
root.geometry("1000x1200")
root.title("Py Flora")

header = tk.Frame(root, bg="#2C3E50", height=70)
header.pack(fill=tk.X)

title = tk.Label(header, text="Py Flora", fg="#FFFFFF", bg="#2C3E50", font=("Helvetica", 24, "bold"))
title.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

sidebar = tk.Frame(root, bg="#34495E", width=150)
sidebar.pack(fill=tk.Y, side=tk.LEFT)

home_btn = tk.Button(sidebar, text="Home", fg="#FFFFFF", bg="#34495E", font=("Helvetica", 14), bd=0, activebackground="#2C3E50")
home_btn.pack(pady=10)

dashboard_btn = tk.Button(sidebar, text="Dashboard", fg="#FFFFFF", bg="#34495E", font=("Helvetica", 14), bd=0, activebackground="#2C3E50")
dashboard_btn.pack(pady=10)

reports_btn = tk.Button(sidebar, text="Reports", fg="#FFFFFF", bg="#34495E", font=("Helvetica", 14), bd=0, activebackground="#2C3E50")
reports_btn.pack(pady=10)

footer = tk.Frame(root, bg="#F1C40F", height=70)
footer.pack(fill=tk.X, side=tk.BOTTOM)

status = tk.Label(footer, text="Status: Connected", fg="#FFFFFF", bg="#F1C40F", font=("Helvetica", 16))
status.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

root.mainloop()
