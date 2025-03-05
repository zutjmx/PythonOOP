import os
import requests

# Variables de ambiente
covid19_host = os.getenv('COVID19_HOST')
covid19_api_key = os.getenv('X_API_KEY_COVID19')

url = "https://covid-19-statistics.p.rapidapi.com/reports/total?date=2020-06-24"

payload = {}
headers = {
  'x-rapidapi-host': covid19_host,
  'x-rapidapi-key': covid19_api_key
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
