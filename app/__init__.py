from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey101"
# app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password101@localhost/project1"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://ejdnlbyrlpjokc:077f1c2b7b2295ef96e99e6db8feccf2f69ae213102a37b9b8ef257c4cfdc623@ec2-54-221-243-211.compute-1.amazonaws.com:5432/d1kl9oaiq3rujv"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['ALLOWED_UPLOADS'] = set(['jpg','png','jpeg'])

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
