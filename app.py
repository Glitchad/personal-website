import sys

from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)


@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    if "freeze" in sys.argv:
        freezer.freeze()
    else:
        app.run(debug=True)
