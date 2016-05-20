from wtforms.fields.html5 import DateField
from wtforms import TextField, BooleanField,Form, TextAreaField, SubmitField, IntegerField, PasswordField, validators
from wtforms.validators import Required, ValidationError
#from wtforms.validators import DataRequired

class ContactForm(Form):
  ci = IntegerField("Cédula de identidad", [validators.Required()])
  username = TextField("Nombre de Usuario", [validators.Required()])
  password = PasswordField("Contraseña", [validators.Required()])
  name = TextField("Nombre", [validators.Required()])
  last_name = TextField("Apellido", [validators.Required()])
  email = TextField("Correo electrónico", [validators.Required()])
  #birthday = DateField('DatePicker', format='%Y-%m-%d')
  submit = SubmitField("Aceptar", [validators.Required()])