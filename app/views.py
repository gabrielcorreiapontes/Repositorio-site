from app import app

@app.route("/")
def index():
    return "No pain no gain"

@app.route("/about")
def about():
    return "<h1 style='color: red'>About!!!!</h1>"
