from flask import Flask, render_template, redirect, request, url_for
from flask.ext.sqlalchemy import SQLAlchemy

#from models import Item, db
 
app = Flask(__name__)      

SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://jtcpp:alpine64@jtcpp.mysql.pythonanywhere-services.com/jtcpp$scanwdb".format(
	username="jtcpp",
	password="alpine64",
	hostname="jtcpp.mysql.pythonanywhere-services.com",
	databasename="jtcpp$scanwdb")
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299

db = SQLAlchemy(app)

class Item(db.Model):
	__tablename__ = 'items'
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
		
 
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "GET":
		return render_template('index.html', itemss=Item.query.all())

	item = Item(content=request.form["items"])
	db.session.add(item)
	db.session.commit()
	return redirect(url_for('index'))
  
@app.route('/register')
def register():
	
	return render_template('register.html')
	
@app.route('/login')
def login():

	return render_template('login.html')
	
@app.route('/dashboard')
def dashboard():

	return render_template('dashboard.html')
#if __name__ == '__main__':
#  app.run(debug=True)