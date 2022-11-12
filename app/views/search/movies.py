from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from package import VersioningEventFacade

search_movies_app = Blueprint('search_movies', __name__)

_search_fold = "search/"
_movie_search_bar_file = _search_fold + "movies_bar.html"

# Find movie page - Initialize menu
@search_movies_app.route('/search/movie/')
def menu():
    print("User is on search movie menu")
    return render_template(_search_fold + 'movies_bar.html')

# Get user movie search and redirect
@search_movies_app.route('/search/movie/', methods = ['POST'])
@search_movies_app.route('/search/movie/<key>', methods = ['POST'])
def input(key = None):
    print("User made a movie search")
    input_text = request.form['movie_title']
    return redirect(url_for("search_movies.results", key = input_text))

# Get the user movie search and find corresponding movies
@search_movies_app.route('/search/movie/<key>')
def results(key = None):
    print("User made '", key, "' movie search")
    results = VersioningEventFacade.search_movies(key)
    if not results:
        return render_template(_search_fold + 'results.html', message = "No movies matches your search", search = key, search_bar = _movie_search_bar_file)
    return render_template(_search_fold + 'results.html', results = results, search = key, search_bar = _movie_search_bar_file)
