from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://onjztqxj:tTUjpYXXAD2TFoF1VZW4vDMC7MUO2DNE@tuffi.db.elephantsql.com/onjztqxj"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


@app.route('/')
def hello():
    return '<h1>!---ONLINE E METENDO----!</h1>'

