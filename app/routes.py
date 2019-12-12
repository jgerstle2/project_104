from app import app
from flask import render_template


# If a user tries to browse to either no page (e.g. www.touro.edu/) or the index page, then call index() below
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home Page")
