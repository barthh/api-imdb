from flask import render_template,request, url_for, redirect
from flask import Blueprint

home_app = Blueprint('home', __name__)

# Main menu
@home_app.route('/')
@home_app.route('/home')
def home():
    return render_template('home.html', menu = "no")

# POST Method when searching a movie
@home_app.route('/', methods = ['POST'])
@home_app.route('/home', methods = ['POST'])
def home_post(key = None):    
    print(request.form["submit"])
    if request.form["submit"] == "Find movies":
        input_text = request.form['movie_title']
        input_method = "search_movies.results"

    elif request.form["submit"] == "Find series":
        input_text = request.form['serie_title']
        input_method = "search_series.results"
    return redirect(url_for(input_method, key = input_text))
