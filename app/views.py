from flask import Flask, render_template
 
@app.route('/')
def index():
  return render_template('index.html')
  
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