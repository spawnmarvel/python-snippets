https://stackoverflow.com/questions/28530918/how-do-i-connect-to-a-kerberos-authenticated-rest-service-in-python-on-windows

The server is giving you a 401 challenge - and the client (usually a browser or even curl) provides the credentials in a subsequent call. If you are already logged in at your domain - try forcing a pre-emptive hop, i.e. you’d carry your Kerberos ticket with your call and the server will not give you a 401 challenge:


https://pypi.org/project/requests-kerberos/

HTTPKerberosAuth can be forced to preemptively initiate the Kerberos GSS exchange and present a Kerberos ticket on the initial request (and all subsequent). By default, authentication only occurs after a 401 Unauthorized response containing a Kerberos or Negotiate challenge is received from the origin server. This can cause mutual authentication failures for hosts that use a persistent connection (eg, Windows/WinRM), as no Kerberos challenges are sent after the initial auth handshake. This behavior can be altered by setting force_preemptive=True:


and also if the error is cannot connect to proxie, we add a dict proxies = {"http": "", "https":""}

