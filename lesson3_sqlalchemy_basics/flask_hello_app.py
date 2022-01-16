from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from helpers import sqlalchemy_config

params = sqlalchemy_config(filename="./database.ini")
print(params)
app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = sqlalchemy_config(filename="./database.ini")
db = SQLAlchemy(app)


class Person(db.Model):
    __tablename__ = 'persons'
    id: int = db.Column(db.Integer, primary_key=True)
    name: str = db.Column(db.String(), nullable=False)

    def __repr__(self):
        return f"<Person ID: {self.id}, name: {self.name}>"


db.create_all()


@app.route("/")
def index():
    person = Person.query.first()
    return_str = """
        <h1>Hello, World from {name}!</h1>
      <p> So a multiline flask by {name}!</p>
      """.format(name=person.name)
    return return_str


# if __name__ == '__main__':
#   print(__name__)   # I add two more lines here
#   print("ok")
#   app.run(debug=True)
