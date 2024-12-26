import json

import requests

from Utilities.configuration import getConfig
from Utilities.resources import ApiResources

url = getConfig()['API']['endpoint'] + ApiResources.getBook

response = requests.get(url, params={'AuthorName': 'Rahul Shetty2'}, )
json_response = response.json()  # will grab the response in json format
print(json_response[0]['book_name'])

assert response.status_code == 200

print(response.headers)  # Will grab the header

assert response.headers['Content-Type'] == "application/json;charset=UTF-8"

for i in json_response:
    if i['isbn'] == '98203':
        print(i)
        break

e = {
    "book_name": "RobotFramework",
    "isbn": "98203",
    "aisle": "324053"
}
assert e == i

'''url = 'https://thinking-tester-contact-list.herokuapp.com/contacts'
r = requests.get(url, headers={
    'Authorization': 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NzY1NzkzMzZhNjU4ODAwMTMxZWE5OTQiLCJpYXQiOjE3MzQ3NzE2MDl9.1ow3mzpT0R-RbqftTA_Wd7uoAvtRlHY72o136Mj7HQQ'}, )
json_response = r.json()
print(json_response)'''
