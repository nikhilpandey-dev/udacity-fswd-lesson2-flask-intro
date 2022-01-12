from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return_str = """
        <h1>Hello, World!</h1
      <p> So a multiline flask!</p>
      """
    return return_str