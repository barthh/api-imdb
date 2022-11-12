from flask import Flask
from .views import *
from flask import render_template, request
from package import imdb_requests_event

app = Flask(__name__)

@app.before_first_request
def activate_job():
    APIkey_message = imdb_requests_event.IMDBRequest.search_movies("leon").errorMessage
    print(APIkey_message)
    return APIkey_message

if (activate_job() == ""):
    app.register_blueprint(home_app)
    app.register_blueprint(information_app)
    app.register_blueprint(search_app)
    print("suceed")
else:
    app.register_blueprint(errorapi_app)
    print("error")


from app.views import error_handlers