from flask import Flask, render_template, request, redirect
from app import app
from app.forms import ContactForm

#@app.route('/')
#@app.route('/index')
#def index():
#        return render_template('index.html',
#                            conf = app.config)

@app.route('/')
@app.route('/index',methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if request.method == 'POST':
		return 'Form posted.'

	elif request.method == 'GET':
		return render_template('contact.html', form=form)