'''
Contact Directory GUI
Nathan Tang
19/01/09
'''

import tkinter as tk
from tkinter import simpledialog
import csv



def newContact(): # Allows user to add new contact
    
    fil = open("contactData.csv", newline='')
    readCSV = csv.reader(fil)
    rows = []

    for line in readCSV:
        rows.append(line)

    fName = simpledialog.askstring("Add New Contact", "First Name:")
    sName = simpledialog.askstring("Add New Contact", "Surname:")
    email = simpledialog.askstring("Add New Contact", "Email:")
    phone = simpledialog.askstring("Add New Contact", "Phone Number:")
    address = simpledialog.askstring("Add New Contact", "Address:")
    birthdate = simpledialog.askstring("Add New Contact", "Birthdate (YYYY/MM/DD):")

    contact = []
    contact.extend([fName, sName, email, phone, address, birthdate])
    rows.append(contact)

    for i in range(len(contact)): # Checks to see if user inputted anything
        if contact[i] == "" or contact[i] is None:
            pass
        else:
            fil = open("contactData.csv", "w", newline="")  # Writes rows to CSV file
            writeCSV = csv.writer(fil)
            for i in range(len(rows)):
                writeCSV.writerow(rows[i])
    

def editContact():
    return


def delContact(tree): # Still not working

    #https://stackoverflow.com/questions/43571715/deleting-selected-items-from-the-treeview-as-well-as-from-the-list-at-the-same

    fil = open("contactData.csv", newline='')
    readCSV = csv.reader(fil)
    rows = []

    for line in readCSV:
        rows.append(line)


    selectedContact = tree.selection()
    for contact in selectedContact:             
        for i in range(len(rows)):
            if rows[i] == contact:
                rows.pop(i) # Remove the corresponding item
                # Make sure the list is updated:
                print('length: {}'.format(len(rows)))
                break
        tree.delete(contact)

    

def printTreeview(tree): # Updates the treeview with CSV data

    fil = open("contactData.csv", newline='')
    readCSV = csv.reader(fil)
    rows = []
    for line in readCSV:
        rows.append(line)

    # tree.delete(*tree.get_children()) # Delete tree to refresh currently not working

    for i in range(len(rows)):
        tree.insert("", i, text=rows[i][0], values=(rows[i][1],rows[i][2],rows[i][3],rows[i][4],rows[i][5]))







'''
NOTE: The code below is currently returning a blank list
'''

# def newContact():

#     def addNewContact():
        
#         contact.append([fName, sName, email, phone, address])


#     root = tk.Tk()
#     root.wm_title("Add New Contact")
    
#     contact = []
    
#     tk.Label(root, pady=3, padx=3, text="First Name").grid(row=0, column=0)
#     tk.Label(root, pady=3, padx=3, text="Surname").grid(row=1, column=0)
#     tk.Label(root, pady=3, padx=3, text="Email").grid(row=2, column=0)
#     tk.Label(root, pady=3, padx=3, text="Phone").grid(row=3, column=0)
#     tk.Label(root, pady=3, padx=3, text="Address").grid(row=4, column=0)


#     fName = tk.Entry(root)
#     sName = tk.Entry(root)
#     email = tk.Entry(root)
#     phone = tk.Entry(root)
#     address = tk.Entry(root)

#     fName.grid(row=0, column=1)
#     sName.grid(row=1, column=1)
#     email.grid(row=2, column=1)
#     phone.grid(row=3, column=1)
#     address.grid(row=4, column=1)

#     fName = fName.get()
#     sName = sName.get()
#     email = email.get()
#     phone = phone.get()
#     address = address.get()

#     tk.Button(root, text="Add", command=addNewContact).grid(row=5)

   
    
#     root.mainloop()
#     print(contact)
#     return contact

    
