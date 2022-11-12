from app import app
from flask import render_template, request
from flask import abort

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error404.html'), 404

@app.errorhandler(500)
def page_not_found(e):
    print(e)
    return render_template("error500.html"), 500