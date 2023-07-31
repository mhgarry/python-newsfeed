from flask import Blueprint, render_template

bp = Blueprint('home', __name__, url_prefix='/')
# create a route to the home page templated in index.html with jinja syntax
@bp.route('/')
def index():
    return render_template('index.html')
# create a route to the login page templated in login.html with jinja syntax with javascript to handle the login form submission
@bp.route('/login')
def login():
    return render_template('login.html')
