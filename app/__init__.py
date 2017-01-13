from flask import Flask
from views import app

app.secret_key = 'alpine'

#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://jtcpp:alpine64@mysql.server/jtcpp$scanwdb'

#from models import db
#db.init_app(app)