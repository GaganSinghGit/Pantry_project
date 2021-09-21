from package import app
from flask import render_template, redirect, url_for, flash
#from package.models import Item, User
from package.forms import RequestForm
from package import db
from flask_login import login_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home_page():
    return render_template('home.html')


@app.route("/request")
def request_page():
    form = RequestForm()

    return render_template('requestForm.html', form = form)
