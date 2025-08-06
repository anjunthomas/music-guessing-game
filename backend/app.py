from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///test.db'         # 3 forward slashes is a relative path, 4 is an absolute path
db = SQLAlchemy(app) #initializing database

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200), nullable=False) #don't want it to be left blank
    #completed = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self): #returns information or official string representation of an object
        return '<Task %r>' % self.id #makes a new element, it returns task and id of task that was created


#creating index route

@app.route('/')
def index():
    return render_template('index.html') #knows to look in templates folder

if __name__ == "__main__":
    app.run(debug=True)