import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('personal-220223-89908fd447b2.json', scope)
client = gspread.authorize(creds)
sheet = client.open_by_key("12EmXZyPwuwqDLqEtwRMgL8L0PSIrEkebqlKxFhyA6zg").sheet1

# Save response from /search in chrome dev tools network tab
with open('resp', 'r') as f:
    j = json.loads(f.read())

# print(j['events']['results'])
counter = 0
for item in j['events']['results']:
    print("Start:", item['start_date'], item['start_time'])
    # print(item['start_time'])
    try:
        print("Price:", item['ticket_availability']['minimum_ticket_price']['display'])
    except Exception:
        pass
    print("Title:", item['name'])
    print(item['url'])
    # print(item)
    print('=================================')
    values = [item['name'], item['start_date'], item['start_time'], item['url']]
    sheet.insert_row(values, index=2, value_input_option='RAW')

    counter += 1
    print(counter)


print(counter)