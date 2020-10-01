# https://pypi.org/project/requests-kerberos/
# https://github.com/requests/requests-kerberos
'''
In order to use this library, there must already be a Kerberos Ticket-Granting Ticket(TGT) cached in a Kerberos credential cache. Whether a TGT is available can be easily determined by running the klist command
Authentication Failures
Client authentication failures will be communicated to the caller by returning the 401 response. A 401 response may also come from an expired Ticket-Granting Ticket.
In short, the library will handle the "negotiations" of Kerberos authentication, but ensuring that an initial TGT is available and valid is the responsibility of the user.
'''
import requests
from requests_kerberos import HTTPKerberosAuth, REQUIRED

url = "......."

response = requests.get(url, auth=HTTPKerberosAuth(), verify= False)

print(response)
print(response.text)
