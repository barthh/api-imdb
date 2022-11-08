from flask import render_template
from flask import abort
from flask import Blueprint
from package import VersioningEventFacade

information_app = Blueprint('information', __name__)

# Display movie rating
@information_app.route('/info/')
@information_app.route('/info/<key>')
def information(key = None):
    if not key:
        abort(404)
    movie = VersioningEventFacade.get_rating(key)
    if not (movie.fullTitle):
        return render_template('information.html', message = "Movie or Serie not found")
    return render_template('information.html', movie = movie)