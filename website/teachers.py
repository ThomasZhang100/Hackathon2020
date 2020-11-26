from website.models import Teacher,Review
from website.__init__ import db
# one = Teacher(name="Mr. Helicopter", grade=9)
# db.session.add(one)
# two = Teacher(name="Ms. Tank", grade=9)
# db.session.add(two)
# three = Teacher(name="Mr. Computer", grade=10)
# db.session.add(three)
# four = Teacher(name="Ms. Peanut", grade=10)
# db.session.add(four)
# five = Teacher(name="Mr. Blaze", grade=11)
# db.session.add(five)
# six = Teacher(name="Ms. Linch", grade=11)
# db.session.add(six)
# seven = Teacher(name="Mr. Linux", grade=12)
# db.session.add(seven)
# eight = Teacher(name="Ms. Ubuntu", grade=12)
#
# db.session.add(eight)
db.session.add(Review(teacher_id=7, content="Mediocre"))
db.session.add(Review(teacher_id=8, content="Cool"))
db.session.commit()

