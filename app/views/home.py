from flask import render_template
from flask import Blueprint

home_app = Blueprint('home', __name__)

# Main menu
@home_app.route('/')
@home_app.route('/home')
def home():
    return render_template('search_bar.html')

from flask import render_template,request


def page_not_found(e):
    print(e)
    return render_template("error.html")
