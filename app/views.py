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
@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
def contact():
	form = ContactForm(request.form)
	if request.method == 'POST':
		new_user = User(form.ci.data,form.name.data,form.last_name.data,form.email.data)
		print(form.ci.data)
		db.session.add(new_user)
		db.session.commit()
		return 'Form posted.'

	elif request.method == 'GET':
		return render_template('contact.html', form=form)