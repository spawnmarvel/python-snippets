https://stackoverflow.com/questions/28530918/how-do-i-connect-to-a-kerberos-authenticated-rest-service-in-python-on-windows

The server is giving you a 401 challenge - and the client (usually a browser or even curl) provides the credentials in a subsequent call. If you are already logged in at your domain - try forcing a pre-emptive hop, i.e. you’d carry your Kerberos ticket with your call and the server will not give you a 401 challenge:

and also if the error is cannot connect to proxie, we add a dict proxies = {"http": "", "https":""}

