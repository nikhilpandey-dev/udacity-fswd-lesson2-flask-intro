from distutils.log import error
from flask import Flask, render_template, request, redirect, url_for, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from helpers import sqlalchemy_config
import sys
from typing import Dict
params = sqlalchemy_config(filename="./database.ini")
print(params)
app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_config(
    filename="./database.ini")
db = SQLAlchemy(app)


migrate = Migrate(app, db)

class Todo(db.Model):
    __tablename__ = 'todos'
    id: int = db.Column(db.Integer, primary_key=True)
    description: str = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Todo {self.id}: {self.description}>"


# db.create_all()


@app.post('/todos/create')
def create_todo():
    is_error = False
    body: Dict[str, str] = dict()
    try:
        description: str = request.get_json()['description'].strip()
        print(f"description is: {description}")
        todo: Todo = Todo(description=description)
        db.session.add(todo)
        if not description:
            db.session.delete(todo)
            db.session.rollback()
        else:
            db.session.commit()
            body['description'] = todo.description
    except:
        is_error = True
        db.session.rollback()
        print(sys.exc_info())
    finally:
        db.session.close()
    
    if is_error:
        abort(400)
    else:
        return jsonify(body)
    


@app.route('/')
def index():
    # Model.query.all() is deprecated and we are expected to us db.session.query(Model).all()
    return render_template('index.html', data=db.session.query(Todo).all())
