from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route("/")
def home():
    if str(datetime.datetime.today()).split()[0] == "2025-12-11":
        return render_template("valentines.html")
    else:
        return render_template("index.html")

app.run(debug=True)
