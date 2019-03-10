'''
Contact Directory GUI
Nathan Tang
19/01/09
'''

import tkinter as tk
from tkinter import simpledialog
import csv
import spreadsheet
import gspread

def openCSV(): # Opens CSV
    fil = open("contactData.csv", newline='')
    readCSV = csv.reader(fil)
    rows = []
    for line in readCSV:
        rows.append(line)

    return rows



def writeCSV(rows): # Writes to CSV
    fil = open("contactData.csv", "w", newline="")  # Writes updated rows to CSV file
    writeCSV = csv.writer(fil)
    for i in range(len(rows)):
        writeCSV.writerow(rows[i])

    return rows

    

def impSpread(): # Import spreadsheet information into list
    rows = spreadsheet.worksheet.get_all_values()
    return rows



def updateSpreadsheet(rows): # Updates the entire Google Spreadsheet
    cells = []
    for row_num, row in enumerate(rows):
        for col_num, cell in enumerate(row):
            cell = cell
            cells.append(gspread.Cell(row_num + 1, col_num + 1, rows[row_num][col_num]))
    spreadsheet.worksheet.update_cells(cells)



def sort(tree, column, descending): # Allows user to sort the data

    data = [(tree.set(child, column), child) for child in tree.get_children('')] # Places values to sort in data

    data.sort(reverse=descending) # Reorders data
    for index, item in enumerate(data):
        tree.move(item[1], '', index)

    tree.heading(column, command=lambda col=column: sort(tree, column, int(not descending)))



def newContact(tree): # Allows user to add new contact
    
    rows = openCSV()

    # Create contacts dialog
    fName = simpledialog.askstring("Add New Contact", "First Name:")
    sName = simpledialog.askstring("Add New Contact", "Surname:")
    email = simpledialog.askstring("Add New Contact", "Email:")
    phone = simpledialog.askstring("Add New Contact", "Phone Number (___-___-____):")
    address = simpledialog.askstring("Add New Contact", "Address:")
    birthdate = simpledialog.askstring("Add New Contact", "Birthdate (YYYY/MM/DD):")

    # Adds data to rows
    contact = []
    contact.extend([fName, sName, email, phone, address, birthdate])
    rows.append(contact)

    for i in range(len(contact)): # Checks to see if user inputted anything
        if contact[i] == "" or contact[i] is None:
            pass
        else:
            rows = writeCSV(rows) # Updates the CSV file

            tree.delete(*tree.get_children()) # Deletes tree

            # Writes updated tree
            for i in range(len(rows)):
                tree.insert("", i, values=(rows[i][0],rows[i][1],rows[i][2],rows[i][3],rows[i][4],rows[i][5]))

    # Inserts new contact into Google Spreadsheet
    spreadsheet.worksheet.insert_row(contact, (len(rows)))



def editContact(tree): # Allows user to edit contact

    rows = openCSV()

    selected_item = tree.selection()[0]

    for i in range(len(rows)):
        if rows[i] == tree.item(selected_item)['values']:

            # Edit contacts dialog
            fName = simpledialog.askstring("Edit Contact", "First Name:", initialvalue=rows[i][0])
            sName = simpledialog.askstring("Edit Contact", "Surname:", initialvalue=rows[i][1])
            email = simpledialog.askstring("Edit Contact", "Email:", initialvalue=rows[i][2])
            phone = simpledialog.askstring("Edit Contact", "Phone Number (___-___-____):", initialvalue=rows[i][3])
            address = simpledialog.askstring("Edit Contact", "Address:", initialvalue=rows[i][4])
            birthdate = simpledialog.askstring("Edit Contact", "Birthdate (YYYY/MM/DD):", initialvalue=rows[i][5])
            
            # Deletes unedited row
            rows.pop(i)
            tree.delete(selected_item)

            # Updates rows with edited data
            contact = []
            contact.extend([fName, sName, email, phone, address, birthdate])
            rows.append(contact)

            for i in range(len(contact)): # Checks to see if user inputted anything
                if contact[i] == "" or contact[i] is None:
                    pass
                else:
                    rows = writeCSV(rows) # Updates the CSV file

                    tree.delete(*tree.get_children()) # Deletes tree

                    # Writes updated tree
                    for i in range(len(rows)):
                        tree.insert("", i, values=(rows[i][0],rows[i][1],rows[i][2],rows[i][3],rows[i][4],rows[i][5]))

            # Updates the Google Spreadsheet
            updateSpreadsheet(rows)
            
        else:
            pass



def delContact(tree): # Deletes the highlighted contact

    '''NOTE: Currently cannot delete list with integers'''

    rows = openCSV()

    selected_item = tree.selection()[0] # Deletes selected item from tree and rows
    treeItem = tree.item(selected_item)['values']
    for i in range(len(rows)):
        if rows[i] == treeItem:
            delIndex = rows.index(treeItem)
            rows.pop(i)
            print(rows)
            break
    tree.delete(selected_item)

    rows = writeCSV(rows) # Updates the CSV file
    spreadsheet.worksheet.delete_row(delIndex+1) # Updates the Google Spreadsheet


def printTreeview(tree): # Updates the treeview with CSV data

    rows = openCSV()

    tree.delete(*tree.get_children()) # Delete tree

    # Writes updated tree
    for i in range(len(rows)):
        tree.insert("", i, values=(rows[i][0],rows[i][1],rows[i][2],rows[i][3],rows[i][4],rows[i][5]))
