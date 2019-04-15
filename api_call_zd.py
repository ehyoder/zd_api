import json

import requests

import config 
session = requests.Session()
session.auth = config.credentials


url = 'https://compassapps.zendesk.com/api/v2/tickets.json?' 
response = session.get(url)
if response.status_code == 200:
    print('Status:', response.status_code, 'Ok')
else:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Assign variable to response data
zd_data = response.json()
# Convert from Python to formatted JSON
with open('zddata.json', 'w') as outfile:
    json.dump(zd_data, outfile)


# Print dictionary keys with data type 
zd_keys = list(zd_data.keys())
for i in zd_keys:
    print(i, type(i))

# Find ticket id for the first ticket
#print(zd_data["tickets"][0]["id"])

# Find ticket comments for the first ticket 
#print(zd_data["tickets"][0]["description"])

# Print data type of tickets 
print(type(zd_data["tickets"]))
