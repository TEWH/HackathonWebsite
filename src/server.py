from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/home")
def hello():
    return render_template("index.html")

@app.route("/loggedIn")
def afterLogin():
    return render_template("afterlogin.html")


if __name__ == "__main__":
    app.run()
