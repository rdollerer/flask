from flask import Flask, abort, request, jsonify
#from werkzeug.exceptions import jsonify
import random

app = Flask(__name__)

@app.route("/hello")
def hello():
  return "Hello World"

"""@app.errorhandler(NotFound)"""
def handler_error404(err):
  return "You have encountered an error of 404",404

app.register_error_handler(404, handler_error404)

@app.route("/age/<val>")
def age(val):
    try:
        return "Hello, I am {} years old".format(int(val))
    except ValueError:
        #raise BadRequest("You did not enter an integer")
        abort(400,description="You did not enter an integer")

@app.route('/random', methods=["POST", "GET"])
def get_random():
    if request.method == "POST":
        data = request.get_json()
        if not data or "name" not in data or "end" not in data:
            abort(400, description="Invalid request payload")

        name = data["name"]
        end = data["end"]

        if not isinstance(end, int):
            abort(400, description="End must be an integer")

        if name == 'Daniel':
            try:
                random_number = random.randint(1, end)
                return jsonify(message=f"Your random number is {random_number}!")
            except ValueError:
                abort(400, description="Invalid end parameter")
        else:
            return jsonify(message="Name is not Daniel"), 403
    else:
        return jsonify(message="Use POST method"), 405


@app.route('/birth', methods=['POST'])
def post_birth():
    data = request.get_json()

    if not data or "name" not in data or "birth_year" not in data:
        abort(400, description="Invalid request payload")

    name = data['name']
    birth_year = data['birth_year']

    if not isinstance(birth_year, int):
        abort(400, description = 'birth_year must be an integer')

    return jsonify(message=f"{name} was born in {birth_year}")