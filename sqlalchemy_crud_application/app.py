from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from helpers import sqlalchemy_config
params = sqlalchemy_config(filename="./database.ini")
print(params)
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_config(
    filename="./database.ini")
db = SQLAlchemy(app)


class Todo(db.Model):
    __tablename__ = 'todos'
    id: int = db.Column(db.Integer, primary_key=True)
    description: str = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Todo {self.id}: {self.description}>"

db.create_all()

@app.post('/todos/create')
def create_todo():
    description = request.form.get('description', '')
    todo = Todo(description=description.strip())
    db.session.add(todo)
    if ''.__eq__(description.strip()):
        db.session.rollback()
    else:
        db.session.commit()
    return redirect(url_for('index'))
    

@app.route('/')
def index():
    # Model.query.all() is deprecated and we are expected to us db.session.query(Model).all()
    return render_template('index.html', data=db.session.query(Todo).all())
