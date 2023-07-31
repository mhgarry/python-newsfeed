from flask import Blueprint, render_template

bp = Blueprint('dashboard'm __name__, url_prefix='/dashboard') # create a blueprint for our dashboard routes

@bp.route('/')
def dash():
    return render_template('dashboard.html')

@bp.route('/edit/<id>')
def edit(id):
    return render_template('edit-post.html')