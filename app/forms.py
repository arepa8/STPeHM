from flask.ext.wtf import Form
from wtforms.fields.html5 import DateField
from wtforms import TextField, BooleanField,Form, TextAreaField, SubmitField, IntegerField, PasswordField
from wtforms.validators import Required

class ContactForm(Form):
  ci = IntegerField("Cédula de identidad")
  username = TextField("Nombre de Usuario")
  password = PasswordField("Contraseña")
  name = TextField("Nombre")
  last_name = TextField("Apellido")
  email = TextField("Correo electrónico")
  #birthday = DateField('DatePicker', format='%Y-%m-%d')
  submit = SubmitField("Agregar usuario")

