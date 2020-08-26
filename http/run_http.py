import http.client

conn = http.client.HTTPSConnection("www.breakingbadapi.com", 443) # accepts a hostname, not url
conn.request("GET", "/api/quotes/1")
response = conn.getresponse()
data = response.read()
print(data)
conn.close()