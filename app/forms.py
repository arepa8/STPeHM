from wtforms.fields.html5 import DateField
from wtforms import TextField, BooleanField,Form, TextAreaField, SubmitField, IntegerField, PasswordField, DateTimeField, validators, SelectField
from wtforms.validators import Required, ValidationError
#from wtforms.validators import DataRequired

class ContactForm(Form):
	ci = IntegerField("Cédula de identidad", [validators.Required()])
	username = TextField("Nombre de usuario", [validators.Required()])
	password = PasswordField("Contraseña", [validators.Required()])
	name = TextField("Nombre", [validators.Required()])
	last_name = TextField("Apellido", [validators.Required()])
	email = TextField("Correo electrónico", [validators.Required()])
	#birthday = DateField('DatePicker', format='%Y-%m-%d')
	role = SelectField("Rol", [validators.Required()], coerce=int)
	submit = SubmitField("Aceptar", [validators.Required()])

class ProfileForm(ContactForm):
	#name = TextField("Nombre", [validators.Required()])
	#last_name = TextField("Apellido", [validators.Required()])
	#email = TextField("Correo electrónico", [validators.Required()])
	sex = SelectField('Sexo',choices=[('F', 'Femenino'), ('M', 'Masculino')])
	date_of_birth = DateField('Fecha de nacimiento', format='%Y-%m-%d')
	marital_status = SelectField('Estado civil', choices=[('soltero', 'Soltero'), ('casado', 'Casado'), ('viudo', 'Viudo'), ('divorciado','Divorciado'), ('Otro','Otro')])
	telephone = TextField("Número de teléfono")
	address = TextField("Dirección", [validators.length(max=500)])
	submit = SubmitField("Modificar", [validators.Required()])

class DoctorProfileForm(ProfileForm):
	habilities = TextField("Habilidades y destrezas", [validators.length(max=500)])
	pregrade = TextField("Pregrado", [validators.length(max=100)])
	postgrade =TextField("Postgrado", [validators.length(max=100)])
	experience =TextField("Experiencia profesional", [validators.length(max=500)])
	courses =TextField("Cursos", [validators.length(max=500)])
	seminars =TextField("Seminarios", [validators.length(max=500)])
	publications =TextField("Publicaciones", [validators.length(max=500)])
	awards =TextField("Reconocimientos", [validators.length(max=500)])
	submit = SubmitField("Modificar", [validators.Required()])


class PatientProfileForm(ProfileForm):
	heigth = TextField("Altura", [validators.length(max=15)])
	weigth = TextField("Peso", [validators.length(max=15)])
	blood_type = SelectField('Tipo de sangre', choices=[('a+', 'A+'),('a-', 'A-'),
														('ab+', 'AB+'),('ab-', 'AB-'),
														('o+', 'O+'),('o-', 'O-') ])
	diabetic = SelectField('Diabético',choices=[('T', 'Sí'), ('F', 'No')])
	allergies = TextField("Reacciones alérgicas", [validators.length(max=500)])
	emergency_contact = TextField("Contacto en caso de emergencia", [validators.length(max=100)])
	emergency_number = TextField("Teléfono en caso de emergencia", [validators.length(max=15)])
	comments = TextField("Comentarios", [validators.length(max=500)])
	submit = SubmitField("Modificar", [validators.Required()])


class ConsultationForm(Form):
	hospital = SelectField("Institución", [validators.Required()], coerce=int)
	especialidad = SelectField("Especialidad", [validators.Required()], coerce=int)
	submit = SubmitField("Agregar", [validators.Required()])

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