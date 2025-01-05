import os
from flask import Flask, jsonify, request  # jsonify pro vracení JSON
from . import db
from flask_restful import Api, Resource, reqparse

app = Flask(__name__)

app.config.from_mapping(
    DATABASE=os.path.join(app.instance_path, 'tourdeflask.sqlite'),
)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

db.init_app(app)

#Argumenty/pravidla pro potrebna data pri tvorbe hry (?)
hra_post_arg = reqparse.RequestParser()
hra_post_arg.add_argument("name", type=str, help="Pojmenování hry", required=True)
hra_post_arg.add_argument("difficulty", type=str, help="Úroveň obtížnosti hry", required=True)
hra_post_arg.add_argument("board", help="Stav mřížky hry", required=True)

@app.route('/')
def hello_world():  # put application's code here
    return "Hello TdA"

#API endpoint pro /api
@app.route('/api', methods=['GET'])
def get_organization():
    return jsonify({"organization": "Student Cyber Games"}) 

#Prvni verze pro API - vytvoreni hry
@app.route('/api/v1', methods=['POST'])
def create_game():
    argumenty = hra_post_arg.parse_args()
    game_data = request.get_json()
    return (argumenty), 201 #Z nejakyho duvodu vraci jen prvni seznam ze seznamu mrizky, nevim a dneska uz neresim

if __name__ == '__main__':
    app.run(debug=True) 
