import os
import pathlib
from flask import Flask, render_template

app = Flask(__name__, instance_relative_config=True)
module_path = os.path.abspath(os.path.dirname(__file__))

@app.route('/')
#@app.route('/index')
def index():
    return '''
    <html>
    <head>
        <title>Home Page</title>
    </head>
    <body>
        <h1>Hello!</h1>
    </body>
    </html>
    '''
    #render_template(f"{module_path}/templates/app/index.html", title="Home")

