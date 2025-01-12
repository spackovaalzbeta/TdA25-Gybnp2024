import os
from flask import Flask, jsonify  # jsonify pro vracení JSON
from . import db
from flask_restful import Api, Resource, reqparse, fields, marshal_with, abort
from flask_sqlalchemy import SQLAlchemy
import uuid

app = Flask(__name__)
api = Api(app)

#app.config.from_mapping(
#    DATABASE=os.path.join(app.instance_path, 'tourdeflask.sqlite'),
#)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///database.db"
db = SQLAlchemy(app)

#db.init_app(app)

# ensure the instance folder exists
#try:
#    os.makedirs(app.instance_path)
#except OSError:
#    pass

class GameModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    difficulty = db.Column(db.String(80), nullable=False)
    board = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"Game(name = {self.name}, difficulty = {self.difficulty}, board = {self.board})"

game_args = reqparse.RequestParser()
game_args.add_argument("name", type=str, required=True, help="Name cannot be blank")
game_args.add_argument("difficulty", type=str, required=True, help="Difficulty cannot be blank")
game_args.add_argument("board", action='append', required=True, help="Board cannot be blank")

gameFields = {
    "id":fields.Integer,
    "name":fields.String,
    "name":fields.String,
    "board":fields.List
}

class Games(Resource):
    @marshal_with(gameFields)
    def get(self): #Vypsani ulozenych her
        games = GameModel.query.all()
        return games
    
    @marshal_with(gameFields)
    def post(self): #Vytvoreni hry
        args = game_args.parse_args()
        game = GameModel(name=args["name"], difficulty=args["difficulty"], board=args["board"])
        db.session.add(game)
        db.session.commit()
        games = GameModel.query.all()
        return games, 201
        
    
api.add_resource(Games, "/api/v1/games/")

@app.route('/')
def hello_world():  # put application's code here
    return "Hello TdA"

#API endpoint pro /api
@app.route('/api', methods=['GET'])
def get_organization():
    return jsonify({"organization": "Student Cyber Games"}) 

if __name__ == '__main__':
    app.run(debug=True) 
