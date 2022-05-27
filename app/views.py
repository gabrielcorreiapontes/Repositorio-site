from app import app

from flask import render_template

@app.route("/")
def index():
    return render_template("/public/index.html")

@app.route("/jinja")
def jinja():
    return render_template("/public/jinja.html")

@app.route("/product")
def products():
    return "<h1 style='color: red'>produtogtx2</h1>"

@app.route("/categories")
def categories():
    return "<h1 style='color: red'>categorias</h1>"

@app.route("/user")
def users():
    return "<h1 style='color: red'>users</h1>"
    
@app.route("/about")
def about():
    return "<h1 style='color: red'>SPP - Sell PC Parts</h1>"
