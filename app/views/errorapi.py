from flask import render_template,request
from flask import Blueprint

errorapi_app = Blueprint('home', __name__)

# Main menu
@errorapi_app.route('/')
@errorapi_app.route('/home')
def home():
    return render_template("errorApiKey.html")