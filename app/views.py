from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy

from sqlalchemy import *
from app import app, lm
from app.forms import ContactForm
from app.models import User, db
from flask.ext.login import login_user, logout_user, current_user, login_required

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
		return render_template('show_users.html', users=users)


@lm.user_loader
def load_user(user_id):
    return User.get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    # Here we use a class of some kind to represent and validate our
    # client-side form data. For example, WTForms is a library that will
    # handle this for us, and we use a custom LoginForm to validate.
    form = ContactForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        login_user(user)

        flask.flash('Logged in successfully.')

        next = flask.request.args.get('next')
        # next_is_valid should check if the user has valid
        # permission to access the `next` url
        if not next_is_valid(next):
            return flask.abort(400)

        return flask.redirect(next or flask.url_for('index'))
    return flask.render_template('login.html', form=form)
