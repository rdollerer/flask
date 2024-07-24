from flask import Flask
from pydantic import BaseModel
from flask_pydantic import validate

class Query(BaseModel):
    name:str
    age:int

class Player(BaseModel):
    name:str
    position:str
    team:str
    birth_year:int

app = Flask(__name__)

@app.route("/intro")
@validate()
def intro(query:Query):
    return "Hello, my name is {} and I am {} years old".format(query.name,query.age)

@app.route("/info")
@validate()
def info(query:Player):
    return query.dict()


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)