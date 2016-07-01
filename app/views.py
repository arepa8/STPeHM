from flask import Flask, render_template, request, redirect, session, flash, url_for
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import *
from app import app, lm
from app.forms import *
from app.models import User,Role,db,Appointment, Institution, Specialization,PatientProfile,DoctorProfile, InstitutionElement, DoctorStudies, DoctorAbilities, DoctorAwards, DoctorPublications, DoctorExperiences, DoctorEvents, FamilyBackground,PathologicalBackground,NonPathologicalBackground,PatientConsultation
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext import admin, login
from flask.ext.admin import helpers, expose
from app.controllers import appointment, user, role, institution, specialization, patientProfile, doctorProfile, familyBackground, pathologicalBackground, nonPathologicalBackground
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

@app.route('/home',methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        active_user = session['user']
        return render_template('home.html', active_user=active_user)


@app.route('/users',methods=['GET', 'POST'])
def show_users():
    if request.method == 'GET':
        users = User.query.all()
        active_user = session['user']
        return render_template('show_users.html', users=users, active_user=active_user)

@app.route('/roles',methods=['GET', 'POST'])
def show_roles():
    if request.method == 'GET':
        active_user = session['user']
        roles = Role.query.all()
        return render_template('show_roles.html', active_user=active_user, roles=roles)

@app.route('/institutions',methods=['GET', 'POST'])
def show_institutions():
    if request.method == 'GET':
        active_user = session['user']
        instituciones = Institution.query.all()
        return render_template('show_institutions.html', active_user=active_user, instituciones=instituciones)

@app.route('/specializations',methods=['GET', 'POST'])
def show_specializations():
    if request.method == 'GET':
        active_user = session['user']
        especializacion = Specialization.query.all()
        return render_template('show_specializations.html', active_user=active_user, especializacion=especializacion)

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
                    return redirect(url_for('home'))
            error = 'Invalid username or password'
        return render_template('index.html', error=error)
    return redirect(url_for('home'))


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
    return render_template('show_roles.html', roles=roles)

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
        return render_template('add_appointment.html', form = form, title= title, active_user=active_user)
    else:
        form = DoctorAppointmentForm(request.form)
        if request.method == 'POST':
            new_a = appointment.appointment()
            if new_a.insertAppointment(form.patient.data,active_user['ci'],form.date.data,form.description.data):
                return redirect(url_for('show_appointments'))
            else:
                print('Error')
        title = "Agregar"
        return render_template('add_appointment.html', form = form, title= title, active_user=active_user)

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
    id = int(id)
    a = appointment.appointment()
    deleted = a.deleteAppointment(id)
    if deleted:
        return json.dumps({'status':'OK','id':id})
    else: 
        return json.dumps({'status':'ERROR','id':id})

#
# GESTIÓN DE INSTITUCIONES
#

@app.route('/add_institution', methods=['GET', 'POST'])
def add_institution():
    ''' Agrega una institución '''
    active_user = session['user']
    form = InstitutionForm(request.form)
    if request.method == 'POST':
        new_i = institution.institution()
        if new_i.insertInstitution(form.name.data,form.address.data):
            return redirect(url_for('show_institutions'))
        else:
            print('Error')
    title = "Agregar"
    return render_template('add_institution.html', active_user=active_user, form=form, title=title)


@app.route('/edit_institution/<id>', methods=['GET', 'POST'])
def edit_institution(id):
    '''Ofrece la parametrización detallada para modificar una institución'''
    active_user = session['user']
    form = InstitutionForm(request.form)
    if request.method == 'POST':
        inst = institution.institution()
        modified = inst.modifyInstitution(id, form.name.data, form.address.data)
        if modified:
            return redirect(url_for('show_institutions'))
        else:
            print("Error")
    old = Institution.query.filter_by(id=id).first()
    form = InstitutionForm(request.form, name=old.name, address=old.address)
    return render_template('edit_institution.html', form=form, id=id, institution = old)



@app.route('/add_mision/<id>', methods=['GET', 'POST'])
def add_mision(id):
    ''' Agrega una institución '''
    active_user = session['user']
    form = InstitutionElementForm(request.form)
    if request.method == 'POST':
        new_ie = InstitutionElement('mision', form.description.data)
        i = Institution.query.filter_by(id=id).first()
        i.elements.append(new_ie)
        db.session.add(new_ie)
        db.session.commit()
        return redirect(url_for('edit_institution',id=id))
    title = "Agregar"
    return render_template('add_institutionElement.html', active_user=active_user, form=form, title=title, id=id,type='mision')


@app.route('/add_vision/<id>', methods=['GET', 'POST'])
def add_vision(id):
    ''' Agrega una institución '''
    active_user = session['user']
    form = InstitutionElementForm(request.form)
    if request.method == 'POST':
        new_ie = InstitutionElement('vision', form.description.data)
        i = Institution.query.filter_by(id=id).first()
        i.elements.append(new_ie)
        db.session.add(new_ie)
        db.session.commit()
        return redirect(url_for('edit_institution',id=id))
    title = "Agregar"
    return render_template('add_institutionElement.html', active_user=active_user, form=form, title=title, id=id,type='vision')


@app.route('/add_value/<id>', methods=['GET', 'POST'])
def add_value(id):
    ''' Agrega una institución '''
    active_user = session['user']
    form = InstitutionElementForm(request.form)
    if request.method == 'POST':
        new_ie = InstitutionElement('value', form.description.data)
        i = Institution.query.filter_by(id=id).first()
        i.elements.append(new_ie)
        db.session.add(new_ie)
        db.session.commit()
        return redirect(url_for('edit_institution',id=id))
    title = "Agregar"
    return render_template('add_institutionElement.html', active_user=active_user, form=form, title=title, id=id,type='value')


@app.route('/add_objective/<id>', methods=['GET', 'POST'])
def add_objetive(id):
    ''' Agrega una institución '''
    active_user = session['user']
    form = InstitutionElementForm(request.form)
    if request.method == 'POST':
        new_ie = InstitutionElement('objetive', form.description.data)
        i = Institution.query.filter_by(id=id).first()
        i.elements.append(new_ie)
        db.session.add(new_ie)
        db.session.commit()
        return redirect(url_for('edit_institution',id=id))
    title = "Agregar"
    return render_template('add_institutionElement.html', active_user=active_user, form=form, title=title, id=id,type='objetive')

@app.route('/add_history/<id>', methods=['GET', 'POST'])
def add_history(id):
    ''' Agrega una institución '''
    active_user = session['user']
    form = InstitutionElementForm(request.form)
    if request.method == 'POST':
        new_ie = InstitutionElement('history', form.description.data)
        i = Institution.query.filter_by(id=id).first()
        i.elements.append(new_ie)
        db.session.add(new_ie)
        db.session.commit()
        return redirect(url_for('edit_institution',id=id))
    title = "Agregar"
    return render_template('add_institutionElement.html', active_user=active_user, form=form, title=title, id=id,type='history')

@app.route('/add_institutionElement/<id>', methods=['GET', 'POST'])
def add_institutionElement(id):
    ''' Agrega una institución '''
    active_user = session['user']
    form = InstitutionElementForm(request.form)
    if request.method == 'POST':
        new_ie = InstitutionElement('other', form.description.data)
        i = Institution.query.filter_by(id=id).first()
        i.elements.append(new_ie)
        db.session.add(new_ie)
        db.session.commit()
        return redirect(url_for('edit_institution',id=id))
    title = "Agregar"
    return render_template('add_institutionElement.html', active_user=active_user, form=form, title=title, id=id,type='other')


@app.route('/delete_institution', methods=['POST'])
def delete_institution():
    ''' Elimina una institución por su id '''
    id =  int(request.json)
    inst = institution.institution()
    deleted = inst.deleteInstitution(id)
    if deleted:
        return json.dumps({'status':'OK','id':id})
    else: 
        return json.dumps({'status':'ERROR','id':id})


@app.route('/show_institution_data', methods=['POST'])
def show_institution_data():
    ''' Muestra una institución por su id '''
    id =  int(request.json)
    inst = Institution.query.filter_by(id = id).first()
    name = inst.name
    address = inst.address
    print(name)
    print(address)
    return json.dumps({'status':'OK','id':id,'name':name,'address':address})


#
# GESTIÓN DE ESPECIALIZACIONES
#
@app.route('/add_specialization', methods=['GET', 'POST'])
def add_specialization():
    ''' Agrega una Especialización '''
    active_user = session['user']
    form = SpecializationForm(request.form)
    if request.method == 'POST':
        new_s = specialization.specialization()
        if new_s.insertSpecialization(form.name.data):
            return redirect(url_for('show_specializations'))
        else:
            print('Error')
    title = "Agregar"
    return render_template('add_specialization.html', active_user=active_user, form=form, title=title)


@app.route('/modify_specialization/<id>', methods=['GET', 'POST'])
def modify_specialization(id):
    ''' Modifica una especialización '''
    active_user = session['user']
    form = SpecializationForm(request.form)
    if request.method == 'POST':
        s = specialization.specialization()
        modified = s.modifySpecialization(id, form.name.data)
        if modified:
            return redirect(url_for('show_specializations'))
        else:
            print("Error")
    title = "Modificar"
    old = Specialization.query.filter_by(id=id).first()
    form = SpecializationForm(request.form, name=old.speciality)
    return render_template('add_specialization.html', form=form, title=title, id=id)


@app.route('/delete_specialization', methods=['POST'])
def delete_specialization():
    ''' Elimina una especialización por su id '''
    id =  int(request.json)
    s = specialization.specialization()
    deleted = s.deleteSpecialization(id)
    if deleted:
        return json.dumps({'status':'OK','id':id})
    else: 
        return json.dumps({'status':'ERROR','id':id})
        
#
# PERFIL DE PACIENTE
#
@app.route('/profile_user', methods=['GET','POST'])
def profile_user():

    active_user = session['user']
    user_controller = user.user()
    u = user_controller.getUser(active_user['username'])
    r = role.role()
    user_role = r.getRole(int(u.role))

    p = patientProfile.patientProfile()
    patient = p.getPatientProfileByCi(u.ci)
    print(patient)
    
    form = PatientProfileForm(request.form)

    if request.method == 'POST': #and form.validate():
        
        result0 = user_controller.updateUser(u.username, u.password, form.name.data, form.last_name.data, form.email.data, int(u.role))

        # Crear perfil de paciente
        if patient == None:
            result1 = p.insertPatientProfile(int(u.ci),form.sex.data,form.date_of_birth.data,form.marital_status.data,
                                        form.telephone.data,form.address.data,form.heigth.data,form.weigth.data,
                                        form.blood_type.data, form.diabetic.data,form.allergies.data,
                                        form.emergency_contact.data,form.emergency_number.data,
                                        form.comments.data)

        # Modificar perfil de paciente
        else:            
            result1 = p.updatePatientProfile (int(u.ci),form.sex.data,form.date_of_birth.data,
                                        form.marital_status.data,form.telephone.data,form.address.data,
                                        form.heigth.data,form.weigth.data,form.blood_type.data,
                                        form.diabetic.data,form.allergies.data,form.emergency_contact.data,
                                        form.emergency_number.data,form.comments.data)           
      
        if result0['result'] and result1:
            active_user['name'] = form.name.data+' '+form.last_name.data
            return render_template('profile.html', form=form, active_user=active_user, mensaje='Exito')
        else:
            return render_template('profile.html', form=form, active_user=active_user, mensaje='Error')
    
    elif request.method == 'GET':

        form.name.data      = u.name
        form.last_name.data = u.last_name
        form.email.data     = u.email

        # Datos de PatientProfile
        if patient != None:
            
            form.sex.data = patient.sex
            form.date_of_birth.data = patient.date_of_birth
            form.marital_status.data = patient.marital_status
            form.telephone.data = patient.telephone
            form.address.data = patient.address

            form.heigth.data = patient.heigth
            form.weigth.data = patient.weigth
            form.blood_type.data = patient.blood_type
            form.diabetic.data = patient.diabetic
            form.allergies.data = patient.allergies
            form.emergency_contact.data = patient.emergency_contact
            form.emergency_number.data = patient.emergency_number
            form.comments.data = patient.comments

        return render_template('profile.html', active_user=active_user, form=form, ci = u.ci, username=u.username)



##########################
# VIEWS NO IMPLEMENTADAS #
##########################

@app.route('/profile_doctor', methods=['GET','POST'])
def profile_doctor():

	active_user = session['user']
	user_controller = user.user()
	u = user_controller.getUser(active_user['username'])
	r = role.role()
	user_role = r.getRole(int(u.role))
	form = ProfileForm(request.form)    
	d = doctorProfile.doctorProfile()
	doctor = DoctorProfile.query.filter_by(ci_user=u.ci).first()

	if request.method == 'POST': #and form.validate():

		result0 = user_controller.updateUser(u.username, u.password, form.name.data, form.last_name.data, form.email.data, int(u.role))

		# Crear perfil de doctor
		if doctor == None:

			result1 = d.insertDoctorProfile(int(u.ci), form.sex.data,form.date_of_birth.data,form.marital_status.data,
			            form.telephone.data, form.address.data)
		# Modificar perfil de doctor
		else:            

			result1 = d.updateDoctorProfile(int(u.ci),form.sex.data, form.date_of_birth.data,form.marital_status.data,
			            form.telephone.data,form.address.data)

		if result0['result'] and result1:
			active_user['name'] = form.name.data+' '+form.last_name.data
			return render_template('profile_doctor.html', form=form, active_user=active_user, mensaje='Exito')
		else:
			return render_template('profile_doctor.html', form=form, active_user=active_user, mensaje='Error')

	elif request.method == 'GET':

		form.name.data      = u.name
		form.last_name.data = u.last_name
		form.email.data     = u.email

		# Datos de DoctorProfile
		if doctor != None:
			form.sex.data = doctor.sex
			form.date_of_birth.data = doctor.date_of_birth
			form.marital_status.data = doctor.marital_status
			form.telephone.data = doctor.telephone
			form.address.data = doctor.address

		studies = DoctorStudies.query.filter_by(ci_user=u.ci)
		abilities = DoctorAbilities.query.filter_by(ci_user=u.ci)
		experiences = DoctorExperiences.query.filter_by(ci_user=u.ci)
		publications = DoctorPublications.query.filter_by(ci_user=u.ci)
		awards = DoctorAwards.query.filter_by(ci_user=u.ci)
		events = DoctorEvents.query.filter_by(ci_user=u.ci)

		return render_template('profile_doctor.html', events=events, studies=studies, abilities=abilities, experiences=experiences, publications=publications, awards=awards, active_user=active_user, form=form, ci = u.ci, username=u.username)

@app.route('/add_study',methods=['GET', 'POST'])
def add_study():
	active_user = session['user']
	form = DoctorStudiesForm(request.form)
	user_controller = user.user()
	u = user_controller.getUser(active_user['username'])

	if request.method == 'POST':
		new_study = DoctorStudies(u.ci,form.studies.data,form.date_of_graduation.data,form.description.data,form.institution.data)
		db.session.add(new_study)
		db.session.commit()
		return redirect(url_for('profile_doctor'))

	title = "Agregar"
	return render_template('add_studies.html', title=title, active_user=active_user, form=form)

@app.route('/modify_study/<id>',methods=['GET', 'POST'])
def modify_study(id):
	active_user = session['user']
	form = DoctorStudiesForm(request.form)
	user_controller = user.user()
	u = user_controller.getUser(active_user['username'])

	if request.method == 'POST':
		old = DoctorStudies.query.filter_by(id=id).first()
		old.title=form.studies.data
		old.date_of_graduation=form.date_of_graduation.data
		old.description=form.description.data
		old.institution=form.institution.data
		db.session.commit()
		return redirect(url_for('profile_doctor'))

	title = "Modificar"
	old = DoctorStudies.query.filter_by(id=id).first()
	form = DoctorStudiesForm(request.form, studies=old.title,date_of_graduation= old.date_of_graduation,description=old.description,institution=old.institution)
	return render_template('add_studies.html', form=form, studies=old.title,date_of_graduation= old.date_of_graduation,description=old.description,institution=old.institution, id=id, title=title)

@app.route('/delete_study/<id>', methods=['GET','POST'])
def delete_study(id):
    ''' Elimina una evento por su id '''
    #id =  int(request.json)
    print (session)
    active_user = session['user']
    user_controller = user.user()
    u = user_controller.getUser(active_user['username'])
    target_study = DoctorStudies.query.filter_by(id=id).first()
    deleted = False
    if target_study:
        db.session.delete(target_study)
        db.session.commit()
        deleted = True

    return redirect(url_for('profile_doctor'))

@app.route('/add_ability',methods=['GET', 'POST'])
def add_ability():
	active_user = session['user']
	form = DoctorAbilitiesForm(request.form)
	user_controller = user.user()
	u = user_controller.getUser(active_user['username'])

	if request.method == 'POST':
		new_ability = DoctorAbilities(u.ci,form.abilities.data,form.description.data)
		db.session.add(new_ability)
		db.session.commit()
		return redirect(url_for('profile_doctor'))

	return render_template('add_abilities.html', active_user=active_user, form=form)

@app.route('/modify_ability/<id>',methods=['GET', 'POST'])
def modify_ability(id):
	active_user = session['user']
	form = DoctorAbilitiesForm(request.form)
	user_controller = user.user()
	u = user_controller.getUser(active_user['username'])

	if request.method == 'POST':
		old = DoctorAbilities.query.filter_by(id=id).first()
		old.title=form.abilities.data
		old.description=form.description.data
		db.session.commit()
		return redirect(url_for('profile_doctor'))

	title = "Modificar"
	old = DoctorAbilities.query.filter_by(id=id).first()
	form = DoctorAbilitiesForm(request.form, abilities=old.title,description=old.description)
	return render_template('add_abilities.html', form=form,abilities=old.title,description=old.description, id=id, title=title)

@app.route('/delete_ability/<id>', methods=['GET','POST'])
def delete_ability(id):
    ''' Elimina una evento por su id '''
    #id =  int(request.json)
    print (session)
    active_user = session['user']
    user_controller = user.user()
    u = user_controller.getUser(active_user['username'])
    target_ability = DoctorAbilities.query.filter_by(id=id).first()
    deleted = False
    if target_ability:
        db.session.delete(target_ability)
        db.session.commit()
        deleted = True

    return redirect(url_for('profile_doctor'))

# BUSCADOR MEDICOS
@app.route('/search_medicos',methods=['GET', 'POST'])
def search_medicos():
    if request.method == 'GET':
        active_user = session['user']
        usuarios = User.query.all()
        result = []
        for user in usuarios:
            if user.role == "1":
                result.append(user)

        return render_template('search.html',result=result, active=active_user)

# BUSCADOR PACIENTES
@app.route('/search_pacientes',methods=['GET', 'POST'])
def search_pacientes():
    if request.method == 'GET':
        active_user = session['user']
        usuarios = User.query.all()
        result = []
        for user in usuarios:
            if user.role != "1":
                result.append(user)

        return render_template('search.html',result=result, active=active_user)

@app.route('/add_award',methods=['GET', 'POST'])
def add_award():
	active_user = session['user']
	form = DoctorAwardsForm(request.form)
	user_controller = user.user()
	u = user_controller.getUser(active_user['username'])
	if request.method == 'POST':
		new = DoctorAwards(u.ci,form.award.data,form.date.data,form.institution.data)
		db.session.add(new)
		db.session.commit()
		return redirect(url_for('profile_doctor'))
	return render_template('add_awards.html', active_user=active_user, form=form)

@app.route('/modify_award/<id>',methods=['GET', 'POST'])
def modify_award(id):
	active_user = session['user']
	form = DoctorAwardsForm(request.form)
	user_controller = user.user()
	u = user_controller.getUser(active_user['username'])

	if request.method == 'POST':
		old = DoctorAwards.query.filter_by(id=id).first()
		old.title=form.award.data
		old.date=form.date.data
		old.institution=form.institution.data
		db.session.commit()
		return redirect(url_for('profile_doctor'))

	title = "Modificar"
	old = DoctorAwards.query.filter_by(id=id).first()
	form = DoctorAwardsForm(request.form, award=old.title,date= old.date,institution=old.institution)
	return render_template('add_awards.html', form=form, award=old.title,date= old.date,institution=old.institution, id=id, title=title)


@app.route('/delete_award/<id>', methods=['GET','POST'])
def delete_award(id):
    ''' Elimina una evento por su id '''
    #id =  int(request.json)
    print (session)
    active_user = session['user']
    user_controller = user.user()
    u = user_controller.getUser(active_user['username'])
    target_award = DoctorAwards.query.filter_by(id=id).first()
    deleted = False
    if target_award:
        db.session.delete(target_award)
        db.session.commit()
        deleted = True

    return redirect(url_for('profile_doctor'))

@app.route('/add_publication',methods=['GET', 'POST'])
def add_publication():
	active_user = session['user']
	form = DoctorPublicationForm(request.form)
	user_controller = user.user()
	u = user_controller.getUser(active_user['username'])
	if request.method == 'POST':
		new = DoctorPublications(u.ci,form.title.data,form.authors.data,form.description.data,form.magazine.data,form.number.data,form.volume.data,form.date.data)
		db.session.add(new)
		db.session.commit()
		return redirect(url_for('profile_doctor'))

	return render_template('add_publications.html', active_user=active_user, form=form)


@app.route('/modify_publication/<id>',methods=['GET', 'POST'])
def modify_publication(id):
	active_user = session['user']
	form = DoctorPublicationForm(request.form)
	user_controller = user.user()
	u = user_controller.getUser(active_user['username'])

	if request.method == 'POST':
		old = DoctorPublications.query.filter_by(id=id).first()
		old.title=form.title.data
		old.authors=form.authors.data
		old.description=form.description.data
		old.magazine=form.magazine.data
		old.number=form.number.data
		old.volume=form.volume.data
		old.date=form.date.data
		db.session.commit()
		return redirect(url_for('profile_doctor'))

	title = "Modificar"
	old = DoctorPublications.query.filter_by(id=id).first()
	form = DoctorPublicationForm(request.form, title=old.title,authors=old.authors,description=old.description,magazine=old.magazine,number=old.number,volume=old.volume,date= old.date)
	return render_template('add_publications.html', form=form, publication=old.title,date= old.date,description=old.description, id=id, title=title)

@app.route('/delete_publication/<id>', methods=['GET','POST'])
def delete_publication(id):
    ''' Elimina una evento por su id '''
    #id =  int(request.json)
    print (session)
    active_user = session['user']
    user_controller = user.user()
    u = user_controller.getUser(active_user['username'])
    target_publication = DoctorPublications.query.filter_by(id=id).first()
    deleted = False
    if target_publication:
        db.session.delete(target_publication)
        db.session.commit()
        deleted = True

    return redirect(url_for('profile_doctor'))

@app.route('/add_experience',methods=['GET', 'POST'])
def add_experience():
	active_user = session['user']
	form = DoctorExperienceForm(request.form)
	user_controller = user.user()
	u = user_controller.getUser(active_user['username'])
	if request.method == 'POST':
		new = DoctorExperiences(u.ci,form.experience.data,form.date_of_start.data,form.date_of_finish.data,form.description.data,form.institution.data)
		db.session.add(new)
		db.session.commit()
		return redirect(url_for('profile_doctor'))
	return render_template('add_experiences.html', active_user=active_user, form=form)

@app.route('/modify_experience/<id>',methods=['GET', 'POST'])
def modify_experience(id):
	active_user = session['user']
	form = DoctorExperienceForm(request.form)
	user_controller = user.user()
	u = user_controller.getUser(active_user['username'])

	if request.method == 'POST':
		old = DoctorExperiences.query.filter_by(id=id).first()
		old.title=form.experience.data
		old.date_of_start=form.date_of_start.data
		old.date_of_finish=form.date_of_finish.data
		old.description=form.description.data
		old.institution=form.institution.data
		db.session.commit()
		return redirect(url_for('profile_doctor'))

	title = "Modificar"
	old = DoctorExperiences.query.filter_by(id=id).first()
	form = DoctorExperienceForm(request.form, experience=old.title,date_of_start= old.date_of_start,date_of_finish= old.date_of_finish,description=old.description,institution=old.institution)
	return render_template('add_experiences.html', form=form, experience=old.title,date_of_start= old.date_of_start,date_of_finish= old.date_of_finish,description=old.description,institution=old.institution, id=id, title=title)

@app.route('/delete_experience/<id>', methods=['GET','POST'])
def delete_experience(id):
    ''' Elimina una evento por su id '''
    #id =  int(request.json)
    print (session)
    active_user = session['user']
    user_controller = user.user()
    u = user_controller.getUser(active_user['username'])
    target_experience = DoctorExperiences.query.filter_by(id=id).first()
    deleted = False
    if target_experience:
        db.session.delete(target_experience)
        db.session.commit()
        deleted = True

    return redirect(url_for('profile_doctor'))

@app.route('/add_event',methods=['GET', 'POST'])
def add_event():
	active_user = session['user']
	form = DoctorEventsForm(request.form)
	user_controller = user.user()
	u = user_controller.getUser(active_user['username'])
	if request.method == 'POST':
		new = DoctorEvents(u.ci,form.event.data,form.date.data,form.description.data,form.institution.data)
		db.session.add(new)
		db.session.commit()
		return redirect(url_for('profile_doctor'))
	return render_template('add_events.html', active_user=active_user, form=form)


@app.route('/modify_event/<id>',methods=['GET', 'POST'])
def modify_event(id):
	active_user = session['user']
	form = DoctorEventsForm(request.form)
	user_controller = user.user()
	u = user_controller.getUser(active_user['username'])

	if request.method == 'POST':
		old = DoctorEvents.query.filter_by(id=id).first()
		old.title=form.event.data
		old.date=form.date.data
		old.description=form.description.data
		old.institution=form.institution.data
		db.session.commit()
		return redirect(url_for('profile_doctor'))

	title = "Modificar"
	old = DoctorEvents.query.filter_by(id=id).first()
	form = DoctorEventsForm(request.form, event=old.title,date= old.date,description=old.description,institution=old.institution)
	return render_template('add_events.html', form=form, event=old.title,date= old.date,description=old.description,institution=old.institution, id=id, title=title)

@app.route('/delete_event/<id>', methods=['GET','POST'])
def delete_event(id):
    ''' Elimina una evento por su id '''
    #id =  int(request.json)
    print (session)
    active_user = session['user']
    user_controller = user.user()
    u = user_controller.getUser(active_user['username'])
    target_event = DoctorEvents.query.filter_by(id=id).first()
    deleted = False
    if target_event:
        db.session.delete(target_event)
        db.session.commit()
        deleted = True

    return redirect(url_for('profile_doctor'))

    # if deleted:
    #     return json.dumps({'status':'OK','id':id})
    # else: 
    #     return json.dumps({'status':'ERROR','id':id})


@app.route('/consultations',methods=['GET', 'POST'])
def show_consultations():
    if request.method == 'GET':
        active_user = session['user']
        consultas = [{'institution': 'Hospital1', 'speciality': 'Especialidad1'}]
        return render_template('show_consultations.html', active_user=active_user, consultations=consultas)

@app.route('/add_consultation',methods=['GET', 'POST'])
def add_consultation():
    if request.method == 'GET':
        active_user = session['user']
        form = ConsultationForm(request.form)
        institution_controller = institution.institution()
        speciality_controller = specialization.specialization()
        institutions = institution_controller.getAllInstitutions()
        specialities = speciality_controller.getAllSpecializations()
        form.hospital.choices = [(str(inst.id),str(inst.name)) for inst in institutions]
        form.especialidad.choices = [(str(speciality.id),str(speciality.speciality)) for speciality in specialities]
    
        return render_template('add_consultation.html', active_user=active_user, form=form)

@app.route('/patient_history', methods=['GET','POST'])
def patient_history():
    mensaje = None
    form = PatientHistoryForm(request.form)
    if request.method == 'POST':
        ci_user = form.ci.data
        user_controller = user.user()

        u = user_controller.getUserByCi(ci_user)
        if u != []:
            r = role.role()
            user_role = r.getRole(int(u.role))

            if user_role.role_name == 'Paciente':

                return  redirect(url_for('patient_background', ci=ci_user))
            else:
                mensaje = "La cédula debe pertenecer a un paciente"
        else:
            mensaje = "Paciente no registrado"
    return render_template('patient_history.html', form=form, mensaje=mensaje)

@app.route('/patient_background/<ci>', methods=['GET','POST'])
def patient_background(ci):

    if request.method == 'GET':

        user_controller = user.user()
        u = user_controller.getUserByCi(int(ci))
        name = u.name
        last_name = u.last_name
        email = u.email

        patient_controller = patientProfile.patientProfile()
        p = patient_controller.getPatientProfileByCi(ci)
        
        if p != None: 
            sex = p.sex
            date_of_birth= p.date_of_birth
            telephone = p.telephone
            address = p.address
        else:
            sex = None
            date_of_birth=None
            telephone=None
            address = None

        patient_form = ProfileForm(request.form)

        old = FamilyBackground.query.filter_by(ci_user=ci).first()
        old1 = PathologicalBackground.query.filter_by(ci_user=ci).first()
        old2 = NonPathologicalBackground.query.filter_by(ci_user=ci).first()
        
        if old != None:
            form = FamilyBackgroundForm(request.form, asthma=old.asthma,
                                                    cancer=old.cancer,
                                                    heartdisease=old.heartdisease,
                                                    diabetes=old.diabetes,
                                                    liverdisease=old.liverdisease,
                                                    hypertension=old.hypertension,
                                                    other=old.other)
        else: 
            form = FamilyBackgroundForm(request.form)
        
        if old1 != None:
            form1= PathologicalBackgroundForm(request.form, current_condition=old1.current_condition,
                                                            surgical_history=old1.surgical_history,
                                                            transfusional_history=old1.transfusional_history,
                                                            allergies=old1.allergies,
                                                            traumatic_history=old1.traumatic_history,
                                                            hospitalizations=old1.hospitalizations,
                                                            addictions=old1.addictions,
                                                            other=old1.other)
        else:
            form1= PathologicalBackgroundForm(request.form)
        
        if old2 != None:
            form2= NonPathologicalBackgroundForm(request.form,defecation=old2.defecation,
                                                            toothbrushing=old2.toothbrushing,
                                                            cigarrettes=old2.cigarrettes,
                                                            years=old2.years,
                                                            beverages=old2.beverages,
                                                            frecuency=old2.frecuency,
                                                            physical_activity=old2.physical_activity,
                                                            frecuency2=old2.frecuency2,
                                                            other=old2.other)
        else:
            form2= NonPathologicalBackgroundForm(request.form)

        
        consultations = PatientConsultation.query.filter_by(ci_patient=ci)
        active_user = session['user']
        ci_doctor = active_user['ci']

    return render_template('patient_background.html',patient_form=patient_form, form=form, form1=form1, form2= form2, ci=ci,
                            name=name,last_name=last_name,email=email,sex=sex,date_of_birth=date_of_birth,
                            telephone=telephone,address=address, consultations=consultations, ci_doctor=ci_doctor)

@app.route('/family_background/<ci>', methods=['GET','POST'])
def family_background(ci):

    form = FamilyBackgroundForm(request.form)
    old = FamilyBackground.query.filter_by(ci_user=ci).first()

    fb_contoller = familyBackground.familyBackground()

    if old == None:
        result = fb_contoller.insertFamilyBackground(int(ci),form.asthma.data,
                                        form.cancer.data,
                                        form.heartdisease.data,
                                        form.diabetes.data,
                                        form.liverdisease.data,
                                        form.hypertension.data,
                                        form.other.data)
    else:
        result = fb_contoller.updateFamilyBackground(int(ci),form.asthma.data,
                                        form.cancer.data,
                                        form.heartdisease.data,
                                        form.diabetes.data,
                                        form.liverdisease.data,
                                        form.hypertension.data,
                                        form.other.data)

    return redirect(url_for('patient_background', ci=ci))

@app.route('/pathological_background/<ci>', methods=['GET','POST'])
def pathological_background(ci):
    
    form= PathologicalBackgroundForm(request.form)
    old = PathologicalBackground.query.filter_by(ci_user=ci).first()

    pb_controller = pathologicalBackground.pathologicalBackground()

    if old == None:
        result = pb_controller.insertPathologicalBackground(int(ci),form.current_condition.data,
                                    form.surgical_history.data,
                                    form.transfusional_history.data,
                                    form.allergies.data,
                                    form.traumatic_history.data,
                                    form.hospitalizations.data,
                                    form.addictions.data,
                                    form.other.data)
    else:

        result = pb_controller.updatePathologicalBackground(int(ci),form.current_condition.data,
                                    form.surgical_history.data,
                                    form.transfusional_history.data,
                                    form.allergies.data,
                                    form.traumatic_history.data,
                                    form.hospitalizations.data,
                                    form.addictions.data,
                                    form.other.data)

    return redirect(url_for('patient_background', ci=ci))

@app.route('/non_pathological_background/<ci>', methods=['GET','POST'])
def non_pathological_background(ci):
    
    form= NonPathologicalBackgroundForm(request.form)
    old = NonPathologicalBackground.query.filter_by(ci_user=ci).first()

    npb_controller = nonPathologicalBackground.nonPathologicalBackground()
    
    if old == None:
        result = npb_controller.insertNonPathologicalBackground(int(ci),form.defecation.data,
                                        form.toothbrushing.data,
                                        form.cigarrettes.data,
                                        form.years.data,
                                        form.beverages.data,
                                        form.frecuency.data,
                                        form.physical_activity.data,
                                        form.frecuency2.data,
                                        form.other.data)
    else:
        result = npb_controller.updateNonPathologicalBackground(int(ci),form.defecation.data,
                                        form.toothbrushing.data,
                                        form.cigarrettes.data,
                                        form.years.data,
                                        form.beverages.data,
                                        form.frecuency.data,
                                        form.physical_activity.data,
                                        form.frecuency2.data,
                                        form.other.data)

    return redirect(url_for('patient_background', ci=ci))

@app.route('/add_patient_consultation/<ci>', methods=['GET','POST'])
def add_patient_consultation(ci):
    form = PatientConsultationForm(request.form)
    title = "Agregar"
    if request.method == 'POST':
        ci_patient = ci
        active_user = session['user']
        ci_doctor = active_user['ci']
        name_doctor = active_user['name']
        new_p_consultation = PatientConsultation(ci_patient,ci_doctor,name_doctor,form.date.data,form.motive.data,form.symptoms.data)
        db.session.add(new_p_consultation)
        db.session.commit()
        return redirect(url_for('patient_background', ci=ci))
    return  render_template('patient_consultation.html', form=form,ci=ci, title=title)

@app.route('/modify_patient_consultation/<id>', methods=['GET','POST'])
def modify_patient_consultation(id):

    old = PatientConsultation.query.filter_by(id=id).first()
    ci = old.ci_patient
    if request.method == 'POST':

        form = PatientConsultationForm(request.form)
        old.date = form.date.data
        old.motive = form.motive.data
        old.symptoms = form.symptoms.data
        db.session.commit()
        return redirect(url_for('patient_background', ci=ci))

    title = "Modificar"
    form = PatientConsultationForm(request.form, date=old.date,motive=old.motive,symptoms=old.symptoms)
    return render_template('patient_consultation.html', form=form,ci=ci,id=id,title=title)
