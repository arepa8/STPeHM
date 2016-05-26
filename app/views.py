from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import *
from app import app, lm
from app.forms import ContactForm, AppointmentForm
from app.models import User,Role,db,Appointment
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext import admin, login
from flask.ext.admin import helpers, expose
import datetime
import json



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
		return redirect ('/')
		
	elif request.method == 'GET':
		return render_template('contact.html', form=form)

@app.route('/users',methods=['GET', 'POST'])
def show_users():
	if request.method == 'GET':
		users = User.query.all()
		print(session)
		active_user = session['user']
		roles = Role.query.all()
		return render_template('show_users.html', users=users, active_user=active_user, roles=roles)

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
	                session['user'] = {'name': user.name+' '+user.last_name,'username': user.username, 'ci': user.ci}
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

@app.route('/modify_user/<ci>', methods=['GET', 'POST'])
def modify_user(ci):
	form = ContactForm(request.form)
	if request.method == 'POST' :#and form.validate():
		user = User.query.filter_by(ci = ci).first()
		if user == None:
			flash('No se encontró el usuario %s.' % ci)
			#return
		user.password = form.password.data
		user.name = form.name.data
		user.last_name = form.last_name.data
		user.email = form.email.data
		db.session.commit()

		return redirect('users')

	elif request.method == 'GET':
		user = User.query.filter_by(ci = ci).first()
		form = ContactForm(request.form, password=user.password, name=user.name, last_name=user.last_name, email=user.email)
		
		return render_template('modify_user.html', form=form, ci=ci, username=user.username, password=user.password)

@app.route('/delete_user', methods=['POST'])
def delete_user():
	ci =  request.json
	print(ci)
	user = User.query.filter_by(ci = ci).first()
	db.session.delete(user)
	db.session.commit()
	#return redirect ('users')
	return json.dumps({'status':'OK','ci':ci})

@app.route('/add_role',methods=['POST'])
def add_role():
	role = request.json
	print(role)
	new_role = Role (role_name=role)
	db.session.add(new_role)
	db.session.commit()
	return json.dumps({'status':'OK','role':role})

@app.route('/view_role',methods=['POST'])
def view_role():
	roles = Role.query.all()
	return render_template('show_users.html', roles=roles)


@app.route('/appointments',methods=['GET', 'POST'])
def show_appointments():
	if request.method == 'GET':
		active_user = session['user']
		appointments = Appointment.query.filter_by(user= active_user['ci']).all()
		return render_template('appointments.html', appointments=appointments, active_user=active_user)

@app.route('/add_appointment',methods=['GET', 'POST'])
def add_appointment():

	form = AppointmentForm(request.form)
	if request.method == 'POST':
		active_user = session['user']
		new_a = Appointment(active_user['ci'],form.date.data,form.description.data)
		db.session.add(new_a)
		db.session.commit()
		return redirect(url_for('show_appointments'))

	else:
		title = "Agregar"
		return render_template('add_appointment.html', form = form, title= title)

@app.route('/modify_appointment/<id>',methods=['GET', 'POST'])
def modify_appointment(id):
	form = AppointmentForm(request.form)
	if request.method == 'POST':
		a = Appointment.query.filter_by(id = id).first()
		a.date = form.date.data
		a.description = form.description.data
		db.session.commit()
		return redirect(url_for('show_appointments'))

	else:
		title = "Modificar"
		a = Appointment.query.filter_by(id = id).first()
		form = AppointmentForm(request.form, date=a.date, description = a.description)
		return render_template('add_appointment.html', form = form, title = title, id = id)

@app.route('/delete_appointment', methods=['POST'])
def delete_appointment():
	id =  request.json
	print(id)
	appointment = Appointment.query.filter_by(id = id).first()
	db.session.delete(appointment)
	db.session.commit()
	#return redirect ('users')
	return json.dumps({'status':'OK','id':id})