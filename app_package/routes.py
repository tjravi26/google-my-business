from flask import render_template
from app_package import app


@app.route('/')
@app.route('/index')
def index():
    return render_template('base.html', title='Home')


@app.route('/accounts')
def accounts():
    return render_template('accounts.html', title='Accounts')


@app.route('/upload')
def upload():
    return render_template('upload.html', title='Upload')


@app.route('/about')
def about():
    return render_template('about.html', title='About')
