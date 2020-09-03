import http.client

# https://docs.python.org/3/library/http.client.html
# GET
conn = http.client.HTTPSConnection("www.breakingbadapi.com", 443) # accepts a hostname, not url
conn.request("GET", "/api/quotes/1")
response = conn.getresponse()
data = response.read()
print(data)
conn.close()


# PUT