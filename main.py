'''
Contact Directory GUI
Nathan Tang
19/01/09
'''

import tkinter as tk
from tkinter import ttk
import csv
import functions



root = tk.Tk()
root.wm_title("Contact Directory")

title = tk.Label(root, font=('Tahoma', 12), text='Contact Directory')
title.pack()



# fil = open("contactData.csv", newline='')
# readCSV = csv.reader(fil)
# rows = []

# for line in readCSV:
#     rows.append(line)



info = tk.Label(root, font=('Tahoma', 8), justify=tk.LEFT, text="Store your contacts' names, emails, phone numbers, addresses, and birthdates")
info.pack()

tree = ttk.Treeview(root) # Treeview

tree["columns"]=("one","two","three","four","five")
tree.column("#0", width=100, minwidth=30)
tree.column("one", width=100, minwidth=30)
tree.column("two", width=150, minwidth=30)
tree.column("three", width=150, minwidth=30)
tree.column("four", width=150, minwidth=30)
tree.column("five", width=100, minwidth=30)

tree.heading("#0",text="First Name",anchor=tk.W)
tree.heading("one", text="Surname",anchor=tk.W)
tree.heading("two", text="Email",anchor=tk.W)
tree.heading("three", text="Phone Number",anchor=tk.W)
tree.heading("four", text="Address",anchor=tk.W)
tree.heading("five", text="Birthdate",anchor=tk.W)

tree.pack(fill="both", expand=True)



addButton = tk.Button(root, text="Add Contacts", command = functions.newContact)
editButton = tk.Button(root, text="Edit Contacts", command = functions.editContact)
delButton = tk.Button(root, text="Delete Contacts", command = functions.delContact(tree))

delButton.pack(side=tk.RIGHT)
editButton.pack(side=tk.RIGHT)
addButton.pack(side=tk.RIGHT)

functions.printTreeview(tree)

root.mainloop()