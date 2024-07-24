from flask import Flask, jsonify, request
from pydantic import BaseModel
from flask_pydantic import validate

class Player(BaseModel):
    name:str
    position:str
    team:str
    birth_year:int

app = Flask(__name__)

@app.route("/info", methods=["POST"])
@validate()
def post_player(body: Player):
    return body.model_dump_json()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
