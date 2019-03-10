# Address Book

This program is an address book created in Python, using Tkinter for its GUI.  It allows the user to add, edit, and delete contacts.  Options include: First name, surname, phone number, email, address, and birthdate.

Contacts are saved within a CSV file on the local host.  This information is also saved on a Google Spreadsheet that uses the Google Drive API in conjunction with _gspread_, an API for calling Google Sheets in Python.

## Requirements

This program requires _gspread_ and _oauth2client_ to be installed.  Use the following command to install:

```
pip install gspread oauth2client
```

## Current Known Bugs
1. If only numbers are entered into the dialog boxes, they cannot be deleted with the delete button/function.  They can only be deleted via the CSV file.  Letters or symbols in combination with numbers will work fine.