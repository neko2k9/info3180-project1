from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = "secretkey101"
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://project1:password101@localhost/project1"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True # added just to suppress a warning

app.config['UPLOAD_FOLDER'] = "./app/static/uploads"
app.config['ALLOWED_UPLOADS'] = set(['jpg','png','jpeg'])

db = SQLAlchemy(app)

app.config.from_object(__name__)
from app import views
