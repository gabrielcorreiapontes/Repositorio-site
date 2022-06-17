from collections import UserString
from html.entities import name2codepoint
from app import app

from flask import render_template, request, redirect

@app.route("/admin/dashboard")
def admin_dashboard():
    return render_template("/admin/dashboard.html")
    
@app.route("/admin/profile")
def admin_profile():
    return "<h1 style='color: red'>Admin profile</h1>"


@app.route("/admin/jinja")
def jinja():

    my_name = "eddu"
    
    products = ["xbox","ps5","car","hd"]

    users = {
                "name": "josé",
                "lastname": "azevedo",
                "email": "ja@gmail.com",
                "password": 3242341,
                "postcodes": [51020260,5520434],
                "products": ["product1","product2"],
                "orders": ["order1","ordedr2"]
            }

    class Gitremote:
        def __init__(self, name, description, url):
            self.name = name
            self.description = description
            self.url= url
        
        def pull(self):
            return f"pullin repo {self.name}"

        def clone(self):
            return f"cloning into {self.url}"

    def repeat(x, qty):
        return x * qty


    my_remote = Gitremote(
        name="Flask jinja",
        description="template design tutorial",
        url="https://github.com/gabrielcorreiapontes/Repositorio-site.git"
    )

    return render_template(
        "/admin/jinja.html", my_name=my_name, users=users, products=products,
        Gitremote=Gitremote, repeat=repeat, my_remote=my_remote
        )

