from flask import Flask

app = Flask(__name__)
app.secret_key = 'alpine'

from app import views