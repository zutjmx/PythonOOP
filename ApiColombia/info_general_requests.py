import requests

url = "https://api-colombia.com/api/v1/Country/Colombia"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
