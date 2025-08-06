from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///'         # 3 forward slashes is a relative path, 4 is an absolute path

#creating index route

@app.route('/')
def index():
    return render_template('index.html') #knows to look in templates folder

if __name__ == "__main__":
    app.run(debug=True)