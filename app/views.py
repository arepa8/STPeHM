from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import *
from app import app
from app.forms import ContactForm
from app.models import User, db

#@app.route('/')
#@app.route('/index')
#def index():
#        return render_template('index.html',
#                            conf = app.config)


#db = SQLAlchemy(app)
@app.route('/',methods=['GET', 'POST'])
def index():
	if request.method == 'GET':
		usuarios = User.query.all()
		for user in usuarios:
			print(user.name)
		return render_template('index.html')

@app.route('/index',methods=['GET', 'POST'])
def contact():
	form = ContactForm(request.form)
	if request.method == 'POST':
		new_user = User(form.ci.data,form.name.data,form.last_name.data,form.email.data)
		db.session.add(new_user)
		db.session.commit()
		return render_template('form_posted.html')

	elif request.method == 'GET':
		return render_template('contact.html', form=form)

@app.route('/users',methods=['GET', 'POST'])
def show_users():
	if request.method == 'GET':
		users = User.query.all()
		return render_template('show_users.html', users=users)

@app.route('/modify_user/<ci>', methods=['GET', 'POST'])
def modify_user(ci):
	form = ContactForm(request.form)
	if request.method == 'POST':
		user = User.query.filter_by(ci = ci).first()
		if user == None:
			flash('No se encontró el usuario %s.' % ci)
			#return
		user.name = form.name.data
		user.last_name = form.last_name.data
		user.email = form.email.data
		db.session.commit()

		users = User.query.all()
		return redirect('users')

	elif request.method == 'GET':
		user = User.query.filter_by(ci = ci).first()
		form = ContactForm(request.form, name=user.name, last_name=user.last_name, email=user.email)
		return render_template('modify_user.html', form=form, ci=ci)
