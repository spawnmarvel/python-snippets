# https://pypi.org/project/requests-kerberos/
# https://github.com/requests/requests-kerberos
'''
In order to use this library, there must already be a Kerberos Ticket-Granting Ticket(TGT) cached in a Kerberos credential cache. Whether a TGT is available can be easily determined by running the klist command
Authentication Failures
Client authentication failures will be communicated to the caller by returning the 401 response. A 401 response may also come from an expired Ticket-Granting Ticket.
In short, the library will handle the "negotiations" of Kerberos authentication, but ensuring that an initial TGT is available and valid is the responsibility of the user.
'''
import requests
from requests_kerberos import HTTPKerberosAuth
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "......."

response = requests.get(url, auth=HTTPKerberosAuth(), verify= False)

# or if proxy error
# proxies = {"http": "", "https":""}


# or if we need the response.text back, the data
# response = requests.get(url, auth=HTTPKerberosAuth(force_preemptive=True), verify= False) 

# may have to run twice or make a initial call first, then make the actual call, or store the token from the first call, 
# if there is a token for more data
# Or it just takes a bit time
# The server is giving you a 401 challenge - and the client (usually a browser or even curl) 
# provides the credentials in a subsequent call. If you are already logged in at your domain 
# - try forcing a pre-emptive hop, i.e. you’d carry your Kerberos ticket with your call and the server will not give you a 401 challenge:
print(response)
print(response.text)
