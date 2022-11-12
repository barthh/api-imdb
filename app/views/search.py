from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from package import VersioningEventFacade

search_app = Blueprint('search', __name__)

# POST Method when searching a movie
@search_app.route('/', methods = ['POST'])
@search_app.route('/home', methods = ['POST'])
@search_app.route('/search/', methods = ['POST'])
@search_app.route('/search/<key>', methods = ['POST'])
def home_post(key = None):    
    if request.form["submit"] == "Submit movie":
        input_text = request.form['movie_title']
        input_method = "search.movie_list"
    elif request.form["submit"] == "Submit serie":
        input_text = request.form['serie_title']
        input_method = "search.serie_list"
    return redirect(url_for(input_method, key = input_text))

# Find movie page - display all movies found
@search_app.route('/search_movie/')
@search_app.route('/search_movie/<key>')
def movie_list(key = None):
    print("search_movies")
    if not key:
        return render_template('search_results.html', message = "Please type something to search")
        
    results = VersioningEventFacade.search_movies(key)

    if not results:
        return render_template('search_results.html', message = "No movies matches your search", search = key)

    return render_template('search_results.html', results = results, search = key)

# Find movie page - display all movies found
@search_app.route('/search_serie/')
@search_app.route('/search_serie/<key>')
def serie_list(key = None):
    print("search_series")
    if not key:
        return render_template('search_results.html', message = "Please type something to search")
        
    results = VersioningEventFacade.search_series(key)

    if not results:
        return render_template('search_results.html', message = "No series matches your search", search = key)

    return render_template('search_results.html', results = results, search = key)
    