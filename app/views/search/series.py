from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import Blueprint
from package import VersioningEventFacade

search_series_app = Blueprint('search_series', __name__)

_search_fold = "search/"
_serie_search_bar_file = _search_fold + "series_bar.html"

# Find serie page - Initialize menu
@search_series_app.route('/search/serie/')
def menu():
    print("User is on search serie menu")
    return render_template(_search_fold + 'series_bar.html')

# Get user serie search and redirect
@search_series_app.route('/search/serie/', methods = ['POST'])
@search_series_app.route('/search/serie/<key>', methods = ['POST'])
def input(key = None):
    print("User made a serie search")
    input_text = request.form['serie_title']
    return redirect(url_for("search_series.results", key = input_text))

# Get the user serie search and find corresponding series
@search_series_app.route('/search/serie/<key>')
def results(key = None):
    print("User made '", key, "' serie search")
    results = VersioningEventFacade.search_series(key)
    if not results:
        return render_template(_search_fold + 'results.html', message = "No series matches your search", search = key, search_bar = _serie_search_bar_file)
    return render_template(_search_fold + 'results.html', results = results, search = key, search_bar = _serie_search_bar_file)