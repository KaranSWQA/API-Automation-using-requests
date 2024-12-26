import requests
from Utilities.resources import *
from payLoad import *
from Utilities.configuration import *

url = getConfig()['API']['endpoint'] + ApiResources.addBook
# headers= {}
query = 'select * from Books'
response = requests.post(url, json=buildPayLoadFromDB(query))

print(response.json())

new = response.json()
k = new['ID']

# Delete API
url1 = getConfig()['API']['endpoint'] + ApiResources.deleteBook
response_deleteBook = requests.post(url1, json={

    "ID": k

}, )

assert response_deleteBook.status_code == 200
kar = response_deleteBook.json()

print(kar["msg"])

# Authentication:
se = requests.session()
se.auth = auth = ("karanshetty1441994@gmail.com", getPassword())
url2 = "https://api.github.com/users"
github_response = se.get(url2, verify=False, )
print(github_response.status_code)

url3 = "https://api.github.com/user/repos"
github_response1 = se.get(url3)
print(github_response.status_code)
