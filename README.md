# python-snippets

## Some useful and some for testing

## API (api_rest with http client)
[Flask docs] https://flask.palletsprojects.com/en/1.1.x/

[Flask API] https://www.flaskapi.org/

[Design Restful API] https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask

[Builtin HTTP.Client]https://docs.python.org/3/library/http.client.html

In api rest:
Run first the server
* run_server.py
* run_http.py




GET ALL
<http.client.HTTPConnection object at 0x03A47160>
{'tasks': [{'desc': 'wash', 't_id': 0}, {'desc': 'eat', 't_id': 1}, {'desc': 'sleep', 't_id': 2}]}
200 OK


GET ID
<http.client.HTTPConnection object at 0x03A471D8>
{'tasks': {'desc': 'eat', 't_id': 1}}
200 OK


GET ID
<http.client.HTTPConnection object at 0x03A47160>
{'tasks': None}
200 OK


DELETE ID
<http.client.HTTPConnection object at 0x03A471D8>
{'tasks': {'DELETE': {'desc': 'eat', 't_id': 1}}}
200 OK


PUT ID
<http.client.HTTPConnection object at 0x03A47160>
{'tasks': {'PUT': 200, 'data': 'b"{\'t_id\': 0, \'desc\': \'work\'}"'}}
200 OK


POST ID
<http.client.HTTPConnection object at 0x03A47208>
{'tasks': {'POST': 200, 'data': 'b\'{"desc": "new day"}\''}}
200 OK