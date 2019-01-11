'''
Contact Directory GUI
Nathan Tang
19/01/09
'''

import tkinter as tk
from tkinter import ttk
import csv

root = tk.Tk()
root.wm_title("Contact Directory")

title = tk.Label(root, font=('Tahoma', 12), text='Contact Directory')
title.grid(row=0)

info = tk.Label(root, font=('Tahoma', 8), justify=tk.LEFT, text="Store your contacts' names, emails, phone numbers, and addresses")
info.grid(row=1)

tree = ttk.Treeview(root)

tree["columns"]=("one","two","three","four","five")
tree.column("#0", width=100, minwidth=100)
tree.column("one", width=100, minwidth=100)
tree.column("two", width=150, minwidth=150)
tree.column("three", width=150, minwidth=150)
tree.column("four", width=150, minwidth=150)
tree.column("five", width=100, minwidth=100)

tree.heading("#0",text="First Name",anchor=tk.W)
tree.heading("one", text="Surname",anchor=tk.W)
tree.heading("two", text="Email",anchor=tk.W)
tree.heading("three", text="Phone Number",anchor=tk.W)
tree.heading("four", text="Address",anchor=tk.W)
tree.heading("five", text="Birthdate",anchor=tk.W)

tree.grid(row=2)
root.mainloop()