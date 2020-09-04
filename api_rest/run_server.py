# https://blog.miguelgrinberg.com/post/designing-a-restful-api-with-python-and-flask
from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)

tasks = [
    {"t_id":0, "desc":"wash" },
    {"t_id":1, "desc":"eat" },
    {"t_id":2, "desc":"sleep" }
]
        

@app.route("/api/tasks", methods=["GET"])
def get_all():
    """ http://localhost:8080/api/tasks """
    return jsonify({'tasks': tasks})

@app.route("/api/tasks/<int:t_id>", methods=["GET"])
def get_id(t_id):
    """ http://localhost:8080/api/tasks/2 """
    result_data = None
    if request.method == "GET":
        for i in tasks:
            if i["t_id"] == t_id:
                result_data = i
    return jsonify({'tasks': result_data})

@app.route("/api/tasks/<int:t_id>", methods=["DELETE"])
def delete_id(t_id):
    """ http://localhost:8080/api/tasks/2 """
    result_data = None
    if request.method == "DELETE":
         for i in tasks:
            if i["t_id"] == t_id:
                result_data = {"DELETE":i}
    return jsonify({'tasks': result_data})

@app.route("/api/tasks/<int:t_id>", methods=["PUT"])
def put_id():
    pass

@app.route("/api/tasks/<int:t_id>", methods=["POST"])
def post_id():
    pass



if __name__ == '__main__':
    app.run(debug=True, port=8080)

