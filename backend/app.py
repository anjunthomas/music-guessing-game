from flask import Flask, render_template, url_for, request, redirect
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

with app.app_context():
    db.create_all()

#creating index route

@app.route('/', methods=['POST', 'GET']) #Get is the default, adding post to send data to database
def index():
    if request.method == 'POST': #if request sent to this route is post
       #return 'Hello'
       task_content = request.form['content'] # task content is = to the contents of the input form
       new_task = Todo(content=task_content) #using class todo to create todo object and pushing it to the database next

       try: # trying to commit it to the database
           db.session.add(new_task)
           db.session.commit()
           return redirect('/') #return redirect back to the index html
       except:
           return 'There was an issue adding your task'

    else:
        tasks = Todo.query.order_by(Todo.date_created).all() #looks at the database contents in the order they were created and return all of them
        return render_template('index.html', tasks=tasks) #knows to look in templates folder
    

#Delete Route
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There was a problem deleting that task'

@app.route('/update/<int:id>', methods=['GET', 'POST']) #getting and then updating the id
def update(id):
    task = Todo.query.get_or_404(id)
    if request.method == 'POST':
        task.content = request.form['content'] #setting tasks content to the content in the form input box

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an issue updating your task'
    else:
        return render_template('update.html', task=task)

if __name__ == "__main__":
    app.run(debug=True)