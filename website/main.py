from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/grade9")
def grade9():
    return render_template("grade9.html")

@app.route("/grade10")
def grade10():
    return render_template("grade10.html")

@app.route("/grade11")
def grade11():
    return render_template("grade11.html")

@app.route("/grade12")
def grade12():
    return render_template("grade12.html")

@app.route("/electives")
def electives():
    return render_template("electives.html")

if __name__ == "__main__":
    app.run()