from flask import Flask
from flask import request

app = Flask(__name__)
user = {}

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/daniel")
def hello_dan():
    return "Hello Daniel!"

@app.route("/json")
def hello_json():
    return {"sequence": "Hello World"}

@app.route("/hello_get/<name>")
def hello_get(name):
  return "Hello {}".format(name)
# Do not consider this line </name>    

@app.route("/hello_post", methods=["POST"])
def hello_post():
    data = request.get_json()
    return "Hello {}\n".format(data['name'])

@app.route("/hello", methods=["POST","GET"])
def hello_post_get():
  if request.method=="POST" :
    data = request.get_json()
    return "Hello {} \n".format(data["name"])
  return "Hello World ! "

@app.route("/users/<id>")
def get_user(id):
    return user[id]

@app.route("/add",methods=["PUT"])
def add_user():
    data = request.get_json()
    user[str(len(user))]=data
    return "User {} has been added to the database.".format(len(user)-1)

@app.route("/update/<id>",methods=["POST"])
def update_user(id):
    if id in user:
        user[id] = request.get_json()
        return "User {} has been modified".format(id)
    return "User {} is missing from the database".format(id) 

@app.route("/delete/<id>",methods=["DELETE"])
def delete_user(id):
    if id in user:
        del user[id]
        return "User {} has been deleted".format(id)
    return "The user {} is absent from the database".format(id) 
