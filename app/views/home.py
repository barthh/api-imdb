from flask import render_template,request
from flask import Blueprint

home_app = Blueprint('home', __name__)

# Main menu
@home_app.route('/')
@home_app.route('/home')
def home():
    return render_template('search_bar.html')