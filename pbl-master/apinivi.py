from flask import Flask,render_template,url_for,redirect,request
from flask import session as usersession
from models.modelnivi import create_user
import os

app = Flask(__name__)
app.config['SECRET_KEY']= 'helllo'

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/index',methods=["POST","GET"])
def index():
	if request.method=='POST':

		user_info={}
		user_info['name'] = request.form['name']
		user_info['email']= request.form['email']
		user_info['Announcement']=request.form['Announcement']
		user= create_user(user_info)
		return render_template('info.html')
	else:
		return render_template('info.html')

	# 	user_info={}

	# 	user_info['name']= request.form['name']
	# 	user_info['email']= request.form['email']
	# 	user_info['Announcement']= request.form['Announcement']
	# 	if session['name']==user['name']:
	# 		if session['email']== user['email']:
	# 	 		if session['Announcement']== user['Announcement']:
	# 	 			create_user(user_info)
	# 	return render_template('info.html')
	# 			# return redirect(url_for('index'))
	# else:
	# 	return render_template('info.html')

@app.route('/info')
def info():
		return render_template('info.html')


if __name__=='__main__':

	app.run(debug=True)




