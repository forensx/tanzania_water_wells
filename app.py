import os

from flask import Flask
from flask import render_template

app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(SECRET_KEY='dev')

# a simple page that says hello
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/analysis')
def analysis():
    return render_template("analysis.html")

@app.route('/team')
def team_page():
    return render_template("team.html")


if __name__ == "__main__":
    app.run(debug=True, threaded = True, use_reloader = True)
