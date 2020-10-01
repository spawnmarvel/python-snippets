from requests_ntlm import HttpNtlmAuth
import requests
import urllib.request, urllib.error, urllib.parse, sys

url = "......"
response = requests.get(url, auth=HttpNtlmAuth(sys.argv[1], sys.argv[2]), verify=False)

print(response.json())