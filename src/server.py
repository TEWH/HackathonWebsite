from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def hello():
    return render_template("index.html")

@app.route("/loggedIn")
def afterLogin():
    return render_template("afterlogin.html")

@app.route("/team_page")
def teampage():
    return render_template("team_page.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == "__main__":
    app.run()
