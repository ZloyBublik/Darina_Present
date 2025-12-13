from flask import Flask, render_template
import datetime
import os
app = Flask(__name__)

@app.route("/")
def home():
    if str(datetime.datetime.today()).split()[0] == "2025-12-11":
        return render_template("valentines.html")
    else:
        return render_template("index.html")

@app.route("/whosaidit")
def whosaidit():
    return render_template("whosaidit.html")

if __name__ == "__main__":
    #port = int(os.environ.get("PORT", 5000))  # Use Render's assigned port
    #app.run(host="0.0.0.0", port=port, debug=True)
    app.run(debug=True)
