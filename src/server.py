from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/home")
def hello():
    name2 = "Alina Schroeder"
    return render_template("index.html", name=name2)

if __name__ == "__main__":
    app.run()