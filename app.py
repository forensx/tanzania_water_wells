import os

from flask import Flask
from flask import render_template
from flask import request
from flask_dropzone import Dropzone
import pandas as pd
basedir = os.path.abspath(os.path.dirname(__file__))


app = Flask(__name__, instance_relative_config=True)
app.config.from_mapping(SECRET_KEY='dev')


# a simple page that says hello
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/team')
def team_page():
    return render_template("team_overlay.html")

@app.route('/upload')
def uploadpage():
    return render_template("upload.html")

"""
@app.route('/analysis')
def analysis()
    return render_template("analysis.html")
"""

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'upload'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_CUSTOM= True,
    DROPZONE_ALLOWED_FILE_TYPE= '.csv',
    DROPZONE_MAX_FILE_SIZE=100,
    DROPZONE_MAX_FILES=30,
    DROPZONE_PARALLEL_UPLOADS=3,  # set parallel amount
    DROPZONE_UPLOAD_MULTIPLE=True,  # enable upload multiple
)

dropzone = Dropzone(app)


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    dfs = []
    if request.method == 'POST':
        for key, f in request.files.items():
            if key.startswith('file'):
                f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
                dfs.append(pd.read_csv("upload/"+f.filename))
                os.remove("upload/"+f.filename)

    return render_template('index.html')

if __name__ == '__main__':
   app.run(debug = True)

