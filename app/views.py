from collections import UserString

from html.entities import name2codepoint

from importlib_metadata import method_cache
from app import app

from flask import render_template, request, redirect
from datetime import datetime



### local DB
#                        aux       aux
# users > products > categories > chats > orders

users = {}
products = {}
categories = {}
chats = {}
orders = {}

# DB users need < orders >, when doing creating users,can bi NIL.
users = {
    "josé": {
        "name": "josé",
        "lastname": "azevedo",
        "email": "ja@gmail.com",
        "password": 3242341,
        "postcodes": [51020260,5520434],
        "products": ["products[teclado novo]", "products[fone]"],
        "orders": ["orders[orderAnaJose]", "orders[orderJoseAna]"]
    },
    "ana": {
        "name": "Ana",
        "lastname": "wth",
        "email": "aw@gmail.com",
        "password": 55555,
        "postcodes": [314235234,3456],
        "products": "[products[mouse razer krak]",
        "orders": ["[orders[orderAnaJose]","[orders[orderJoseAna]"]
    }
}


# DB products need < categories >, when doing creating product.
products = {
    "mouse razer krak": {
        "name": "mouse razer krak",
        "categorie": "categories[mouse]",
        "seller": users["ana"],
        "price": 57.87,
        "quantity": 2,
        "quality": "new",
        "postcodes": 314235234,
        "description": "new buy in eua"
    },

    
    "teclado razer": {
        "name": "teclado razer",
        "categorie": "categories[keyboard]",
        "seller": users["ana"],
        "price": 150,
        "quantity": 1,
        "quality": "seminew",
        "postcodes": 314235234,
        "description": "very very good new"
    },

    "teclado novo": {
        "name": "teclado novo",
        "categorie": "categories[keyboard]",
        "seller": users["josé"],
        "price": 100,
        "quantity": 1,
        "quality": "seminew",
        "postcodes": 51020260,
        "description": "semi new but good word"
    },    
    "fone 7.1": {
        "name": "fone 7.1",
        "categorie": "categories[headset]",
        "seller": users["josé"],
        "price": 350,
        "quantity": 4,
        "quality": "seminew",
        "postcodes": 51020260,
        "description": "semi new but good word like the teclado"
    }
}


# DB categories
categories = {

    "keyboard": { 
        "name": "keyboard",
        "products": [products["teclado razer"],products["teclado razer"]]
    },
    "mouse":  { 
        "name": "mouse",
        "products": [products["mouse razer krak"]]
        },
    "headset": { 
        "name": "headset",
        "products":  [products["fone 7.1"]]
        }
}


# DB chats
chats = {
    "mensagesAnaJose1": {
        "seller":users["ana"],
        "buyer": users["josé"],
        "mensage": "hi",
        "datetime": "10:00 24/06/22"
    },
    "mensagesJoseAna1": {
        "seller": users["josé"],
        "buyer": users["ana"],
        "mensage": "I want to know who many day you can delivery to me?",
        "datetime": "14:00 25/06/22"
    },
        "mensagesAnaJose2": {
        "seller": users["ana"],
        "buyer": users["josé"],
        "mensage": "Maybe Today!",
        "datetime": "16:00 25/06/22"
    },
    "mensagesJoseAna2": {
        "seller": users["josé"],
        "buyer": users["ana"],
        "mensage": "Ok,so i want to buy, please.",
        "datetime": "18:30 25/06/22"
    }

}



# DB orders
orders = {
    "orderAnaJose": {
        "seller": users["ana"],
        "buyer": users["josé"],
        "price": 57.87,
        "mensages": [chats["mensagesAnaJose1"],chats["mensagesJoseAna1"],chats["mensagesAnaJose2"],chats["mensagesJoseAna2"]],
        "status": "open",
        "products": [products["mouse razer krak"]]
    },
    "orderJoseAna": {
        "seller": users["josé"],
        "buyer": users["ana"],
        "price": 450,
        "mensages": [chats["mensagesAnaJose1"],chats["mensagesJoseAna1"],chats["mensagesAnaJose2"],chats["mensagesJoseAna2"]],
        "status": "close",
        "products": [products["fone 7.1"],products["teclado novo"]]
    },

}


# clean date time
@app.template_filter("clean_date")
def clean_date(dt):
    return dt.strtime("%d %b %f")

# < home > index
@app.route("/")
def index():
    return render_template("/public/index.html")


# < sign-up > in app
@app.route("/sign-up", methods=["GET", "POST"])
def sign_up():

    if request.method == "POST":
        req = request.form 

        username = req["username"]
        email = req.get("email")
        password = request.form["password"]

        print(username, email, password)

        return redirect(request.url)


    return render_template("public/sign_up.html")

 
# < profile > acess a profile in app
@app.route("/profile/<username>")
def profile(username):

    user = None

    if username in users:
        user = users[username]

    return render_template(
    "/public/profile.html", products=products, categories=categories, username=username, user=user,
    orders=orders
    )

# < categories > acess a  profile in app
@app.route("/categorie/<categoriename>")
def categorie(categoriename):
    return render_template(
    "/public/categorie.html", products=products, categories=categories, users=users,
    orders=orders
    )


# < product > acess profile in app
@app.route("/product/<productname>")
def product(productname):
    
    return render_template(
    "/public/product.html", products=products, categories=categories, users=users,
    orders=orders
    )


# < chat > acess profile in app
@app.route("/profile/<username>/<chatname>")
def chat(username,chatname):
        return render_template(
    "/public/chat.html", products=products, categories=categories, users=users,
    orders=orders,chats=chats
    )



# < order > acess profile in app
@app.route("/profile/<username>/<ordername>")
def order(username,ordername):
        return render_template(
    "/public/order.html", products=products, categories=categories, users=users,
    orders=orders,chats=chats
    )



# < about > the app 
@app.route("/about")
def about():
    return render_template("/public/about.html")