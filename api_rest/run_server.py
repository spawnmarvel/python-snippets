# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response


app = Flask(__name__)

tasks = [
    {"t_id":0, "desc":"wash" },
    {"t_id":1, "desc":"eat" },
    {"t_id":2, "desc":"sleep" }
]
        

@app.route("/api/tasks", methods=["GET"])
def get_all():
    """ http://localhost:8080/api/tasks """
    return jsonify({"tasks": tasks})

@app.route("/api/tasks/<int:t_id>", methods=["GET"])
def get_id(t_id):
    """ http://localhost:8080/api/tasks/2 """
    result_data = None
    if request.method == "GET":
        for i in tasks:
            if i["t_id"] == t_id:
                result_data = i
    return jsonify({"tasks": result_data})

@app.route("/api/tasks/<int:t_id>", methods=["DELETE"])
def delete_id(t_id):
    """ http://localhost:8080/api/tasks/2 """
    result_data = None
    if request.method == "DELETE":
         for i in tasks:
            if i["t_id"] == t_id:
                result_data = {"DELETE":i}
    return jsonify({"tasks": result_data})

@app.route("/api/tasks/<int:t_id>", methods=["PUT"])
def put_id(t_id):
    result_data = None
    if request.method == "PUT":
        # Use request.get_json() to get posted JSON data.
        # rv = request.get_json()
        # Use request.form to get data when submitting a form with the POST method.
        # rv = request.form.get('name', '')
        # Use request.args to get data passed in the query string of the URL, like when submitting a form with the GET method.
        # rv = request.args.get("name", "")

        # The raw data is passed in to the Flask application from the WSGI server as request.stream. The length of the stream is in the Content-Length header.
        length = request.headers["Content-Length"]
        rv = request.get_data()
        new_data = str(rv)
        # add new data
        print("update this data " + new_data)
        print(str(rv) + str(length))
        result_data = {"PUT":200, "data":new_data}

    return jsonify({"tasks": result_data})


@app.route("/api/tasks", methods=["POST"])
def post_id():
    result_data = None
    if request.method == "POST":
        # Use request.get_json() to get posted JSON data.
        # rv = request.get_json()
        # Use request.form to get data when submitting a form with the POST method.
        # rv = request.form.get('name', '')
        # Use request.args to get data passed in the query string of the URL, like when submitting a form with the GET method.
        # rv = request.args.get("name", "")

        # The raw data is passed in to the Flask application from the WSGI server as request.stream. The length of the stream is in the Content-Length header.
        length = request.headers["Content-Length"]
        rv = request.get_data()
        new_data = str(rv)
        # add new data
        print("adding this data " + new_data)
        print(str(rv) + str(length))
        result_data = {"POST":200,"data":new_data}

    return jsonify({"tasks": result_data})



@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True, port=8080)

