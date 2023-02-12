from flask import Flask, render_template
import datetime

app = Flask(__name__)


@app.route("/")
def home():
    time_now = datetime.datetime.now().year
    return render_template("index.html", year=time_now)


if __name__ == "__main__":
    app.run()

