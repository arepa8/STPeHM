from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import *
from app import app, lm
from app.forms import ContactForm, PatientAppointmentForm, DoctorAppointmentForm
from app.models import User,Role,db,Appointment
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext import admin, login
from flask.ext.admin import helpers, expose
from app.controllers import appointment, user, role
import datetime
import json

# GESTION DE USUARIOS
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

# GESTION DE ROLES
@app.route('/add_role',methods=['POST'])
def add_role():
	name = request.json
	new_role = role.role()
	created = new_role.createRole(name)
	if created == True: 
		return json.dumps({'status':'OK','role':name})
	else:
		return json.dumps({'status':'ERROR','role':name, 'error':created})

@app.route('/view_role',methods=['POST'])
def view_role():
	roles = Role.query.all()
	return render_template('show_users.html', roles=roles)

@app.route('/modify_role',methods=['POST'])
def modify_role():
	getrole = request.json
	id = getrole['id']
	name = getrole['name']
	print(getrole, id, name)
	new_role = role.role()
	modified = new_role.updateRole(id,name)
	if modified == True:
		return json.dumps({'status':'OK','role':name})
	else:
		return json.dumps({'status':'ERROR','role':name, 'error':modified})

@app.route('/delete_role',methods=['POST'])
def delete_role():
	id = request.json
	print(id)
	new_role = role.role()
	deleted = new_role.deleteRole(id)
	if deleted == True:
		return json.dumps({'status':'OK','id':id})
	else:
		return json.dumps({'status':'ERROR','id':id})

# GESTION DE CITAS
@app.route('/appointments',methods=['GET', 'POST'])
def show_appointments():
	if request.method == 'GET':
		active_user = session['user']
		a = appointment.appointment()
		if active_user['role'] != 'Medico':
			appointments = a.getAppointmentsByPatient(active_user['ci'])
		else:
			appointments = a.getAppointmentsByDoctor(active_user['ci'])
		return render_template('appointments.html', appointments=appointments, active_user=active_user)

@app.route('/add_appointment',methods=['GET', 'POST'])
def add_appointment():
	active_user = session['user']
	if active_user['role'] != 'Medico':
		form = PatientAppointmentForm(request.form)
		if request.method == 'POST':
			new_a = appointment.appointment()
			if new_a.insertAppointment(active_user['ci'],form.doctor.data,form.date.data,form.description.data):
				return redirect(url_for('show_appointments'))
			else:
				print('Error')
		title = "Agregar"
		return render_template('add_appointment.html', form = form, title= title)
	else:
		form = DoctorAppointmentForm(request.form)
		if request.method == 'POST':
			new_a = appointment.appointment()
			if new_a.insertAppointment(form.patient.data,active_user['ci'],form.date.data,form.description.data):
				return redirect(url_for('show_appointments'))
			else:
				print('Error')
		title = "Agregar"
		return render_template('add_appointment.html', form = form, title= title)

@app.route('/modify_appointment/<id>',methods=['GET', 'POST'])
def modify_appointment(id):
	active_user = session['user']
	if active_user['role'] == 'Paciente':
		form = PatientAppointmentForm(request.form)
		if request.method == 'POST':
			a = appointment.appointment()
			modified = a.modifyAppointment(id, form.date.data, form.description.data)
			if modified:
				return redirect(url_for('show_appointments'))
			#else:
				#MENSAJE DE ERROR
		title = "Modificar"
		a = Appointment.query.filter_by(id = id).first()
		form = PatientAppointmentForm(request.form,doctor=a.doctor, date=a.date, description = a.description)
		return render_template('add_appointment.html', form = form, title = title, id = id)
	else:
		form = DoctorAppointmentForm(request.form)
		if request.method == 'POST':
			a = appointment.appointment()
			modified = a.modifyAppointment(id, form.date.data, form.description.data)
			if modified:
				return redirect(url_for('show_appointments'))
			#else:
				#MENSAJE DE ERROR
		title = "Modificar"
		a = Appointment.query.filter_by(id = id).first()
		form = DoctorAppointmentForm(request.form,patient=a.patient, date=a.date, description = a.description)
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