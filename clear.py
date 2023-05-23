import requests

datas = {}
r = requests.put('https://api.jsonstorage.net/v1/json/4eed805d-59cf-4ff8-ad3b-faf98c316270/c0e5a20d-e108-45d2-9097-19ef727e7af4?apiKey=a2ddf8a1-e69b-4a56-84be-ed30fa49a6ad',data='{}',headers = {"Content-type": "application/json"})
print(r)