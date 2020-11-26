from datetime import datetime
from website.__init__ import db


class Teacher(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	grade = db.Column(db.Integer, nullable=False)
	reviews = db.relationship('Review', backref='teacher', lazy=True)

	def __repr__(self):
		return f"User('{self.name}', '{self.image_file}')"

class Review(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	# date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	teacher_id = db.Column(db.Integer, db.ForeignKey('teacher.id'), nullable=False)

	def __repr__(self):
		return f"Post('{self.content}')"
