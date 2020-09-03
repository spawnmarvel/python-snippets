# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
# https://www.flaskapi.org/
#!flask/bin/python
from flask import Flask
from flask_api import FlaskAPI
# Flask API is a drop-in replacement for Flask that provides an implementation of browsable APIs similar to what Django REST framework provides. 
# It gives you properly content negotiated-responses and smart request parsing:

app = FlaskAPI(__name__)

@app.route('/')
def index():
    return {"Hello world, use route":"/api"}

@app.route('/api')
def api_main():
    return {"You are her":"/api"}

if __name__ == '__main__':
    app.run(debug=True)