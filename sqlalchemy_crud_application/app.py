from flask import Flask, render_template
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

@app.route('/')
def index():
    # Model.query.all() is deprecated and we are expected to us db.session.query(Model).all()
    return render_template('index.html', data=db.session.query(Todo).all())
