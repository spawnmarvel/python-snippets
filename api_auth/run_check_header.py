import requests
import urllib.request, urllib.error, urllib.parse, sys
import urllib3
from requests_kerberos import HTTPKerberosAuth
from time import time
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

import logging
logging.basicConfig(filename="backend.log", level=logging.INFO)


def www_auth(response):
   auth_fields = {}
   for field in response.headers.get("www-authenticate", "").split(","):
      kind, __, details = field.strip().partition(" ")
      auth_fields[kind.lower()] = details.strip()
   return auth_fields


def verify_url(url):
   proxies = {"http": "", "https":""}
   r = requests.get(url,proxies=proxies, verify=False)
   logging.info(r.status_code)
   logging.info(www_auth(r))
   st = r.status_code == 401 and www_auth(r).get('negotiate') == ''
   logging.info(st)
   
   