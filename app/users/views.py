from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import abort
from flask import Blueprint
from app.users.models import PRODUCTS
import package

movie_app = Blueprint('moviefinder', __name__)

# Main menu
@movie_app.route('/')
@movie_app.route('/home')
def home():
    return render_template('search_menu.html')

# POST Method when searching a movie
@movie_app.route('/', methods = ['POST'])
@movie_app.route('/home', methods = ['POST'])
@movie_app.route('/find/', methods = ['POST'])
@movie_app.route('/find/<key>', methods = ['POST'])
def home_post(key = None):
    input_text = request.form['movie_title']    
    return redirect(url_for('moviefinder.movie_list', key = input_text))

# Find movie page - display all movies found
@movie_app.route('/find/')
@movie_app.route('/find/<key>')
def movie_list(key = None):
    if not key:
        return render_template('find.html', message = "Please type something to search")
    movies = package.VersioningEventFacade.get_movies(key)
    if not movies:
        return render_template('find.html', message = "No movies matches your search")
    return render_template('find.html', movies = movies)

# Display movie rating
@movie_app.route('/movie/')
@movie_app.route('/movie/<key>')
def movie_info(key = None):
    if not key:
        abort(404)

    movie = package.VersioningEventFacade.get_rating(key)
    if not (movie.fullTitle):
        return render_template('movie.html', message = "Movie not found")
    return render_template('movie.html', movie = movie)
