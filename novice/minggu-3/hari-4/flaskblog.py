from datetime import datetime
from flask import Flask,render_template,flash,redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.model):
    id = db.column(db.integer,primary_key=True)
    username=db.column(db.string(20),unique = True,nullable=False)
    username=db.column(db.string(120),unique = True,nullable=False)
    image_file=db.column(db.string(20),nullable=False,default='default.jpg')
    password=db.column(db.string(60),nullable=False)
    posts=db.relationship('post',backref='author',lazy=True)

    def __repr__(self):
        return f"user('{self.username}','{self.email}','{self.image_file})"

class post(db.Model):
    id = db.column(db.integer,primary_key=True)
    title = db.column(db.string(100),nullable=False)
    date_posted=db.column(db.dateTime,nullable=False,default=datetime.utcnow)
    content=db.column(db.Text,nullable=False)
    user_id=db.column(db.integer,db.foreignkey('user.id'),nullable=False)

    def __repr__(self):
        return f"post('{self.title}','{self.date_posted}')"