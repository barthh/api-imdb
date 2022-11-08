from flask import Flask
from .views import *

app = Flask(__name__)
app.register_blueprint(home_app)
app.register_blueprint(information_app)
app.register_blueprint(search_app)