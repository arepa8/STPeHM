from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import *
from app import app, lm
from app.forms import ContactForm
from app.models import User, db
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext import admin, login
from flask.ext.admin import helpers, expose

#@app.route('/')
#@app.route('/index')
#def index():
#        return render_template('index.html',
#                            conf = app.config)


#db = SQLAlchemy(app)
# @app.route('/',methods=['GET', 'POST'])
# def index():
# 	if request.method == 'GET':
# 		usuarios = User.query.all()
# 		for user in usuarios:
# 			print(user.name)
# 		return render_template('index.html')

@app.route('/index',methods=['GET', 'POST'])
def contact():
	form = ContactForm(request.form)
	if request.method == 'POST':
		new_user = User(form.ci.data,form.username.data,form.password.data,form.name.data,form.last_name.data,form.email.data)
		db.session.add(new_user)
		db.session.commit()
		return render_template('form_posted.html')

	elif request.method == 'GET':
		return render_template('contact.html', form=form)

@app.route('/users',methods=['GET', 'POST'])
def show_users():
	if request.method == 'GET':
		users = User.query.all()
		print(session)
		active_user = session['user']
		return render_template('show_users.html', users=users, active_user=active_user)


# route for handling the login page logic
@app.route('/', methods=['GET', 'POST'])
def login():
    if 'user' not in session:
	    error = None
	    if request.method == 'POST':
	        userName     = request.form['username']
	        userPassword = request.form['password']

	        # Se busca en la base de datos
	        user = User.query.filter_by(username=userName).first()

	        if user:
	            if user.password == userPassword:
	                # Mostramos el nombre en la aplicación
	                session['user'] = {'name': user.name+' '+user.last_name,'username': user.username}
	                session['logged_in'] = True
	                flash('You were logged in')
	                return redirect(url_for('show_users'))
	        error = 'Invalid username or password'
	    return render_template('index.html', error=error)
    return redirect(url_for('show_users'))

@app.route('/logout')
def logout():
	session.pop('user',None)
	session.pop('logged_in',None)
	return redirect(url_for('login'))
