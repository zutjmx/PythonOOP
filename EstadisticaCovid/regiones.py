import os
import http.client

# Variables de ambiente
covid19_host = os.getenv('COVID19_HOST')
covid19_api_key = os.getenv('X_API_KEY_COVID19')

conn = http.client.HTTPSConnection("covid-19-statistics.p.rapidapi.com")
payload = ''
headers = {
  'x-rapidapi-host': covid19_host,
  'x-rapidapi-key': covid19_api_key
}
conn.request("GET", "/regions", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
