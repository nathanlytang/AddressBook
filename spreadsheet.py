import gspread
import pygsheets
import pprint
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
        'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
# creds = pygsheets.authorize(service_file='client_secret.json')
# client = gspread.authorize(creds)
# client = pygsheets.authorize(service_file='client_secret.json')

# sheet = client.open('Address Book').sheet1

# worksheet = sheet.get_all_records()
gc = gspread.authorize(creds)
# pp = pprint.PrettyPrinter()
# pp.pprint(worksheet)
worksheet = gc.open('Address Book').sheet1
cells = worksheet.get_all_values()
print(cells)