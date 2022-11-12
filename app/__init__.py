from flask import Flask
from package import imdb_requests_event
from .views import *

app = Flask(__name__)

@app.before_first_request
def activate_job():
    APIkey_message = imdb_requests_event.IMDBRequest.search_movies("leon").errorMessage
    return APIkey_message

if (activate_job() == ""):
    app.register_blueprint(home_app)
    app.register_blueprint(information_app)
    app.register_blueprint(search_series_app)
    app.register_blueprint(search_movies_app)
    print("Success")
else:
    app.register_blueprint(errorapi_app)
    print("Problem API key")

from .views import error_handlers