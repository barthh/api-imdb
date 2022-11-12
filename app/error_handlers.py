from app import app
from flask import render_template, request

@app.errorhandler(404)
def page_not_found(e):
    print(e)
    return render_template("error404.html")

@app.errorhandler(500)
def page_not_found(e):
    print(e)
    return render_template("error500.html")