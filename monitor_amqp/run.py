import requests
from requests.auth import HTTPBasicAuth

auth=HTTPBasicAuth('Username', 'Password')

# every thing after ? in the URL is for filtering purposes
URL = "http://localhost:15672/api/definitions?columns=bindings.routing_key"

r = requests.get(url=URL,auth=auth)
# extracting data in json format
data = r.json()

print(data)