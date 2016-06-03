from wtforms.fields.html5 import DateField
from wtforms import TextField, BooleanField,Form, TextAreaField, SubmitField, IntegerField, PasswordField, DateTimeField, validators, SelectField
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
	role = SelectField("Rol", [validators.Required()], coerce=int)
	submit = SubmitField("Aceptar", [validators.Required()])

class ProfileForm(Form):
	name = TextField("Nombre", [validators.Required()])
	last_name = TextField("Apellido", [validators.Required()])
	email = TextField("Correo electrónico", [validators.Required()])
	birthday = DateField('DatePicker', format='%Y-%m-%d')
	hospital = SelectField("Institucion", [validators.Required()], coerce=int)
	especialidad = SelectField("Especialidad", [validators.Required()], coerce=int)
	submit = SubmitField("Modificar", [validators.Required()])

class PatientAppointmentForm(Form):
	doctor = IntegerField("Cédula de indentidad del doctor", [validators.Required()])
	date = DateField("Fecha", [validators.Required()])
	description = TextField("Descripción", [validators.Required(), validators.length(max=500)])
	submit = SubmitField("Aceptar",[validators.Required()])

class DoctorAppointmentForm(Form):
	patient = IntegerField("Cédula de indentidad del paciente", [validators.Required()])
	date = DateField("Fecha", [validators.Required()])
	description = TextField("Descripción", [validators.Required(), validators.length(max=500)])
	submit = SubmitField("Aceptar",[validators.Required()])

class InstitutionForm(Form):
	name = TextField("Nombre", [validators.Required(), validators.length(max=500)])
	address = TextField("Dirección", [validators.Required(), validators.length(max=500)])
	submit = SubmitField("Aceptar",[validators.Required()])

class SpecializationForm(Form):
	name = TextField("Nombre", [validators.Required(), validators.length(max=500)])
	submit = SubmitField("Aceptar",[validators.Required()])