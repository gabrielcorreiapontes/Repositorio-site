from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "No pain no gain"

if __name__ == "__main__":
    app.run()