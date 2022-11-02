from flask import Flask, request
from app.users.views import movie_app

app = Flask(__name__)
app.register_blueprint(movie_app)