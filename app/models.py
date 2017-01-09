from flask.ext.sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class Item(db.Model):
	__table__name = 'Item'
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(45))
	price = db.Column(db.String(10))
	quantity = db.Column(db.Integer)
	description = db.Column(db.String(5000))
	date = db.Column(db.String(10))
	
	def __init__(self, name, price, description, date):
		self.name = name.title()
		self.price = price.title()
		self.description = description.title()
		self.date = date.title()