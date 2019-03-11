# Address Book

This program is an address book created in Python, using Tkinter for its GUI.  It allows the user to add, edit, and delete contacts.  Options include: First name, surname, phone number, email, address, and birthdate.

![GUI Image](https://raw.githubusercontent.com/natt1604/AddressBook/master/images/GUI.png)


Contacts are saved within a CSV file on the local host.  This information is also saved on a Google Spreadsheet that uses the Google Drive API in conjunction with _gspread_, an API for calling Google Sheets in Python.

## Requirements

This program requires _gspread_ and _oauth2client_ to be installed.  Use the following command to install:

```
pip install gspread oauth2client
```

## Usage

1. Install dependencies 

`
pip install gspread oauth2client
`

2. Clone the repository

`
git clone https://github.com/natt1604/AddressBook
`

3. Set up your credentials

On [Google Developers](https://console.developers.google.com), create a new project and enable the Google Drive API. 

![Create Credentials](https://raw.githubusercontent.com/natt1604/AddressBook/master/images/cred0.png "Create Credentials")

Click __Create Credentials__

![Create Credentials](https://raw.githubusercontent.com/natt1604/AddressBook/master/images/cred1.png "Create Credentials")

![Create Credentials](https://raw.githubusercontent.com/natt1604/AddressBook/master/images/cred2.png "Create Credentials")

Copy the settings in the two images above.  Then, download the .json file to the repository.  Share your Google Sheets document with the email provided in the .json file.  In _spreadsheets.py_, replace _client_secret.json_ with the name of your .json file.

## Current Known Bugs
1. If only numbers are entered into the dialog boxes, they cannot be deleted with the delete button/function.  They can only be deleted via the CSV file.  Letters or symbols in combination with numbers will work fine.