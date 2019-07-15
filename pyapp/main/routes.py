from flask import Blueprint, render_template, request
from flask_login import login_required

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    return render_template('home.html')


@main.route("/dashboard")
@login_required
def dashboard():
    return render_template('dashboard-main.html', title='Dashboard')
