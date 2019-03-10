'''
Address Book GUI in Tkinter
Nathan Tang
'''

import tkinter as tk
from tkinter import ttk
import csv
import functions


# Init
root = tk.Tk()
root.wm_title("Contact Directory")



# Title and information
title = tk.Label(root, font=('Tahoma', 12), text='Contact Directory')
title.pack()

info = tk.Label(root, font=('Tahoma', 8), justify=tk.LEFT, text="Store your contacts' names, emails, phone numbers, addresses, and birthdates")
info.pack()

container = ttk.Frame()
container.pack(fill='both', expand=True)



# Treeview
treeColumns = ("First Name","Surname","Email","Phone Number","Address","Birthdate")
tree = ttk.Treeview(columns=treeColumns, show="headings")

for column in treeColumns:
    tree.heading(column, text=column, command=lambda c=column: functions.sort(tree, c, 0))

for i in treeColumns:
    tree.column(i, width=130, minwidth=30)

vsb = ttk.Scrollbar(orient="vertical", command=tree.yview) # Vertical scroll bar
hsb = ttk.Scrollbar(orient="horizontal", command=tree.xview) # Horizontal scroll bar

tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

vsb.grid(column=1, row=0, sticky='ns', in_=container)
hsb.grid(column=0, row=1, sticky='ew', in_=container)
tree.grid(column=0, row=0, sticky='nsew', in_=container)

container.grid_columnconfigure(0, weight=1)
container.grid_rowconfigure(0, weight=1)



# Buttons
addButton = tk.Button(root, text="Add Contacts", command = lambda: functions.newContact(tree))
editButton = tk.Button(root, text="Edit Contacts", command = lambda: functions.editContact(tree))
delButton = tk.Button(root, text="Delete Contacts", command = lambda: functions.delContact(tree))

delButton.pack(side=tk.RIGHT)
editButton.pack(side=tk.RIGHT)
addButton.pack(side=tk.RIGHT)


initRows = functions.impSpread()
rows = functions.writeCSV(initRows)
functions.printTreeview(tree)

root.mainloop()