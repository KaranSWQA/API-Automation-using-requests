import requests

'''res = requests.get("https://httpbin.org/cookies", cookies={'visit-year': '2022'}, allow_redirects=False, timeout=1)
# print(res.history) # will add any redirection before hitting the URL
print(res.text)
print(res.status_code)

se = requests.session()
se.cookies.update({'visit-year': 'FEB'})

res = se.get("https://httpbin.org/cookies", cookies={'visit-year': '2022'})
print(res.text)'''

# Attachment
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open('C:\\Users\\shett\\Downloads\\SQL_1.png', 'rb')}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
