'''
Contact Directory GUI
Nathan Tang
19/01/09
'''

import tkinter as tk

root = tk.Tk()
root.wm_title("Contact Directory")

title = tk.Label(root, 
                font=('Tahoma', 12), 
                text='Contact Directory')

info = tk.Label(root, 
                font=('Tahoma', 8), 
                justify=tk.LEFT,
                text="Store your contacts' names, emails, phone numbers, and addresses")

title.pack()
info.pack()


root.mainloop()