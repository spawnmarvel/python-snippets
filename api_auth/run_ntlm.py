from requests_ntlm import HttpNtlmAuth
import requests
import urllib.request, urllib.error, urllib.parse, sys

url = "......"
# run_ntlm user password
response = requests.get(url, auth=HttpNtlmAuth(sys.argv[1], sys.argv[2]), verify=False)

# or if proxy error
# proxies = {"http": "", "https":""}
# response = requests.get(url,proxies=proxies, auth=HttpNtlmAuth(sys.argv[1], sys.argv[2]), verify=False)


print(response.json())