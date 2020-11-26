from flask import Flask, redirect, url_for, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from website.models import Teacher,Review

app = Flask(__name__)
app.config['SECRET_KEY'] = '6361628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)

def rendergrade(grade):
	teacher_list = []
	teachers = Teacher.query.filter_by(grade=grade).all()

	# convert that list of objects into a Python dict - teacher_list
	for teacher in teachers:
		print(teacher.grade, teacher.name, teacher.id)
		review_list = []
		reviews = Review.query.filter_by(teacher_id=teacher.id).all()
		for review in reviews:
			reviews_dict = {
				"content": review.content
			}
			review_list.append(reviews_dict)
		teacher_dict = {
			"image": teacher.image_file,
			"grade": teacher.grade,
			"name": teacher.name,
			"review_list": review_list
		}
		teacher_list.append(teacher_dict)
	grade = str(grade)+"th Grade"
	return render_template("grade12.html", teachers=teacher_list, grade=grade)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/grade9")
def grade9():
	teacher_list = []
	teachers = Teacher.query.filter_by(grade=9).all()

	# convert that list of objects into a Python dict - teacher_list
	for teacher in teachers:
		print(teacher.grade, teacher.name, teacher.id)
		review_list = []
		reviews = Review.query.filter_by(teacher_id=teacher.id).all()
		for review in reviews:
			reviews_dict = {
				"content": review.content
			}
			review_list.append(reviews_dict)
		teacher_dict = {
			"image": teacher.image_file,
			"grade": teacher.grade,
			"name": teacher.name,
			"review_list": review_list
		}
		teacher_list.append(teacher_dict)
	return render_template("grade12.html", teachers=teacher_list, grade="9th Grade")

@app.route("/grade10")
def grade10():
	teacher_list = []
	teachers = Teacher.query.filter_by(grade=10).all()

	# convert that list of objects into a Python dict - teacher_list
	for teacher in teachers:
		print(teacher.grade, teacher.name, teacher.id)
		review_list = []
		reviews = Review.query.filter_by(teacher_id=teacher.id).all()
		for review in reviews:
			reviews_dict = {
				"content": review.content
			}
			review_list.append(reviews_dict)
		teacher_dict = {
			"image": teacher.image_file,
			"grade": teacher.grade,
			"name": teacher.name,
			"review_list": review_list
		}
		teacher_list.append(teacher_dict)
	return render_template("grade12.html", teachers=teacher_list, grade="10th Grade")

@app.route("/grade11")
def grade11():
	teacher_list = []
	teachers = Teacher.query.filter_by(grade=11).all()

	# convert that list of objects into a Python dict - teacher_list
	for teacher in teachers:
		print(teacher.grade, teacher.name, teacher.id)
		review_list = []
		reviews = Review.query.filter_by(teacher_id=teacher.id).all()
		for review in reviews:
			reviews_dict = {
				"content": review.content
			}
			review_list.append(reviews_dict)
		teacher_dict = {
			"image": teacher.image_file,
			"grade": teacher.grade,
			"name": teacher.name,
			"review_list": review_list
		}
		teacher_list.append(teacher_dict)
	return render_template("grade12.html", teachers=teacher_list, grade="11th Grade")

@app.route("/grade12")
def grade12():
	teacher_list = []
	teachers = Teacher.query.filter_by(grade=12).all()
	
	# convert that list of objects into a Python dict - teacher_list
	for teacher in teachers:
		print(teacher.grade,teacher.name,teacher.id)
		review_list = []
		reviews=Review.query.filter_by(teacher_id=teacher.id).all()
		for review in reviews:
			reviews_dict = {
				"content": review.content
			}
			review_list.append(reviews_dict)
		teacher_dict = {
		"image": teacher.image_file,
		"grade": teacher.grade,
		"name": teacher.name,
		"review_list": review_list
		}
		teacher_list.append(teacher_dict)
	return render_template("grade12.html", teachers=teacher_list, grade="12th Grade")

@app.route("/electives")
def electives():
	teacher_list = []
	teachers = Teacher.query.filter_by(grade=0).all()

	# convert that list of objects into a Python dict - teacher_list
	for teacher in teachers:
		print(teacher.grade, teacher.name, teacher.id)
		review_list = []
		reviews = Review.query.filter_by(teacher_id=teacher.id).all()
		for review in reviews:
			reviews_dict = {
				"content": review.content
			}
			review_list.append(reviews_dict)
		teacher_dict = {
			"image": teacher.image_file,
			"grade": teacher.grade,
			"name": teacher.name,
			"review_list": review_list
		}
		teacher_list.append(teacher_dict)
	return render_template("grade12.html", teachers=teacher_list, grade="Electives")