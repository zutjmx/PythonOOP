import http.client

conn = http.client.HTTPSConnection("api-colombia.com")
payload = ''
headers = {}
conn.request("GET", "/api/v1/TouristicAttraction", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
