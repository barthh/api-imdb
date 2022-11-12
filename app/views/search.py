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
    input_text = request.form['movie_title']   
    return redirect(url_for('search.movie_list', key = input_text))

# Find movie page - display all movies found
@search_app.route('/search/')
@search_app.route('/search/<key>')
def movie_list(key = None):
    if not key:
        return render_template('search_results.html', message = "Please type something to search")
        
    results = VersioningEventFacade.search_movies(key)

    if not results:
        return render_template('search_results.html', message = "No movies matches your search", search = key)

    return render_template('search_results.html', results = results, search = key)