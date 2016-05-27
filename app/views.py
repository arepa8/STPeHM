from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import *
from app import app, lm
from app.forms import ContactForm, AppointmentForm
from app.models import User,Role,db,Appointment
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext import admin, login
from flask.ext.admin import helpers, expose
from app.controllers import appointment, user
import datetime
import json

@app.route('/index',methods=['GET', 'POST'])
def contact():
	form = ContactForm(request.form)
	form.role.choices = [(r.id,r.role_name) for r in Role.query.order_by('role_name')]
	if request.method == 'POST':
		new_user = user.user()
		print(form.role.data)
		result = new_user.insertUser(form.ci.data,form.username.data,form.password.data,form.name.data,form.last_name.data,form.email.data,form.role.data)
		
		if result['result']:
			return redirect(url_for('login'))
		else:
			return render_template('contact.html', form=form, mensaje=result['message'])

	elif request.method == 'GET':
		return render_template('contact.html', form=form)

@app.route('/users',methods=['GET', 'POST'])
def show_users():
	if request.method == 'GET':
		users = User.query.all()
		print(session)
		active_user = session['user']
		roles = Role.query.all()
		return render_template('show_users.html', users=users, active_user=active_user, roles=roles,userRole=active_user['role'])

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

	                # Mostramos y asignamos el nombre del rol.
	                role = None
	                if user.role == '1': role = 'Medico'
                	if user.role == '2': role = 'Paciente'
                	if user.role == '3': role = 'Administrador'

	                session['user'] = {'name': user.name+' '+user.last_name,'username': user.username, 'ci': user.ci, 'role': role}
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
	form.role.choices = [(r.id,r.role_name) for r in Role.query.order_by('role_name')]
	if request.method == 'POST' :#and form.validate():
		user = User.query.filter_by(ci = ci).first()
		if user == None:
			flash('No se encontró el usuario %s.' % ci)
			#return
		user.password = form.password.data
		user.name = form.name.data
		user.last_name = form.last_name.data
		user.email = form.email.data
		user.role = form.role.data
		db.session.commit()

		return redirect('users')

	elif request.method == 'GET':
		user = User.query.filter_by(ci = ci).first()
		form = ContactForm(request.form, password=user.password, name=user.name, last_name=user.last_name, email=user.email)
		form.role.choices = [(r.id,r.role_name) for r in Role.query.order_by('role_name')]

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
		a = appointment.appointment()
		appointments= a.getAppointments(active_user['ci'])
		return render_template('appointments.html', appointments=appointments, active_user=active_user)

@app.route('/add_appointment',methods=['GET', 'POST'])
def add_appointment():

	form = AppointmentForm(request.form)
	if request.method == 'POST':
		active_user = session['user']
		new_a = appointment.appointment()
		if new_a.insertAppointment(active_user['ci'],form.date.data,form.description.data):
			return redirect(url_for('show_appointments'))
		#else
		# MENSAJE DE ERROR
	title = "Agregar"
	return render_template('add_appointment.html', form = form, title= title)

@app.route('/modify_appointment/<id>',methods=['GET', 'POST'])
def modify_appointment(id):
	form = AppointmentForm(request.form)
	if request.method == 'POST':
		a = appointment.appointment()
		modified = a.modifyAppointment(id, form.date.data, form.description.data)
		if modified:
			return redirect(url_for('show_appointments'))
		#else:
			#MENSAJE DE ERROR
	title = "Modificar"
	a = Appointment.query.filter_by(id = id).first()
	form = AppointmentForm(request.form, date=a.date, description = a.description)
	return render_template('add_appointment.html', form = form, title = title, id = id)

@app.route('/delete_appointment', methods=['POST'])
def delete_appointment():
	id =  request.json
	a = appointment.appointment()
	deleted = a.deleteAppointment(id)
	if deleted:
		return json.dumps({'status':'OK','id':id})
	else: 
		return json.dumps({'status':'ERROR','id':id})