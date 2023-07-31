from flask import Blueprint, render_template # import Blueprint and render_template from flask
# Blueprint allows us to consolidate our routes into a single object that we can register in our application, it is equivalent to the express router
# render_template allows us to render html tempaltes with jinja syntax and responds with a template isntead of a string
# with this code we are creating a module to be used in our routes package that will be imported in our __init__.py file


bp = Blueprint('home', __name__, url_prefix='/')
# create a route to the home page templated in index.html with jinja syntax
@bp.route('/')
def index():
    return render_template('index.html')
# create a route to the login page templated in login.html with jinja syntax with javascript to handle the login form submission
@bp.route('/login')
def login():
    return render_template('login.html')

@bp.route('/post/<id>') # <id> is a dynamic route that represents a post id that we define in the post function using id as an argument
def post(id):
    return render_template('single-post.html') 

