from flask import Flask, redirect, url_for, render_template, make_response
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '6361628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

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
	teacher_list = []
	teachers = Teacher.query.filter_by(grade=12).all()
	
	# convert that list of objects into a Python dict - teacher_list
	for teacher in teachers:
		teacher_dict = {
		"image": teacher.image_file,
		"grade": teacher.grade,
		"name": teacher.name,
		}
		teacher_list.append(teacher_dict)
	return render_template("grade12.html", teachers=teacher_list)

@app.route("/electives")
def electives():
    return render_template("electives.html")