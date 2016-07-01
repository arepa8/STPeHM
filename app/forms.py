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
	role = SelectField("Rol", [validators.Required()], coerce=int)
	submit = SubmitField("Aceptar", [validators.Required()])

class ProfileForm(ContactForm):
	sex = SelectField('Sexo',choices=[('F', 'Femenino'), ('M', 'Masculino')])
	date_of_birth = DateField('Fecha de nacimiento', format='%Y-%m-%d')
	marital_status = SelectField('Estado civil', choices=[('soltero', 'Soltero'), ('casado', 'Casado'), ('viudo', 'Viudo'), ('divorciado','Divorciado'), ('Otro','Otro')])
	telephone = TextField("Número de teléfono")
	address = TextField("Dirección", [validators.length(max=500)])

class DoctorStudiesForm(Form):
	studies = TextField("Estudios", [validators.length(max=500)])
	date_of_graduation = DateField("Fecha de culminación", [validators.Required()])
	description =TextField("Descripción", [validators.length(max=100)])
	institution =TextField("Institución", [validators.length(max=500)])
	submit = SubmitField("Aceptar", [validators.Required()])

class DoctorAbilitiesForm(Form):
	abilities = TextField("Habilidad", [validators.length(max=500)])
	description =TextField("Descripción", [validators.length(max=100)])
	submit = SubmitField("Aceptar", [validators.Required()])

class DoctorAwardsForm(Form):		
	award = TextField("Reconocimiento", [validators.length(max=500)])
	date = DateField("Fecha", [validators.Required()])
	institution =TextField("Institución", [validators.length(max=500)])
	submit = SubmitField("Aceptar", [validators.Required()])

class DoctorEventsForm(Form):		
	event = TextField("Evento", [validators.length(max=500)])
	date = DateField("Fecha", [validators.Required()])
	institution =TextField("Institución", [validators.length(max=500)])
	description =TextField("Descripción", [validators.length(max=100)])
	submit = SubmitField("Aceptar", [validators.Required()])

class DoctorPublicationForm(Form):		
	title = TextField("Título", [validators.length(max=100)])
	authors = TextField("Autores", [validators.length(max=100)])
	description =TextField("Descripción", [validators.length(max=500)])
	magazine =TextField("Revista", [validators.length(max=100)])
	number =TextField("Número", [validators.length(max=5)])
	volume =TextField("Volumen", [validators.length(max=5)])
	date = DateField("Fecha", [validators.Required()])
	submit = SubmitField("Aceptar", [validators.Required()])

class DoctorExperienceForm(Form):
	experience =TextField("Puesto Ocupado", [validators.length(max=500)])
	date_of_start = DateField("Fecha de inicio", [validators.Required()])
	date_of_finish = DateField("Fecha de culminación")
	description =TextField("Descripción", [validators.length(max=100)])
	institution =TextField("Institución", [validators.length(max=500)])
	submit = SubmitField("Aceptar", [validators.Required()])
				
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

class InstitutionElementForm(Form):
	name = TextField("Nombre", [validators.Required(), validators.length(max=500)])
	description = TextField("Descripción", [validators.Required(), validators.length(max=500)])
	submit = SubmitField("Aceptar",[validators.Required()])

class SpecializationForm(Form):
	name = TextField("Nombre", [validators.Required(), validators.length(max=500)])
	submit = SubmitField("Aceptar",[validators.Required()])

class PatientHistoryForm(Form):
	ci = IntegerField("Cédula de identidad", [validators.Required()]) 
	submit = SubmitField("Aceptar",[validators.Required()])	

class FamilyBackgroundForm(Form):
	asthma = BooleanField("Asma")
	cancer = BooleanField("Cáncer")
	heartdisease = BooleanField("Cardiopatía")
	diabetes = BooleanField("Diábetes")
	liverdisease = BooleanField("Hepatopatía")
	hypertension = BooleanField("Hipertensión")
	other = TextField("Otro", [validators.length(max=500)])
	submit = SubmitField("Aceptar",[validators.Required()])

class PathologicalBackgroundForm(Form):
	current_condition = TextField("Enfermedades actuales", [validators.length(max=500)])
	surgical_history = TextField("Antecedentes quirúgicos", [validators.length(max=500)])
	transfusional_history = TextField("Antecedentes transfusionales", [validators.length(max=500)])
	allergies = TextField("Alergias", [validators.length(max=500)])
	traumatic_history = TextField("Antecedentes traumáticos", [validators.length(max=500)])
	hospitalizations = TextField("Hospitalizaciones", [validators.length(max=500)])
	addictions = TextField("Adicciones", [validators.length(max=500)])
	other = TextField("Otro", [validators.length(max=500)])
	submit = SubmitField("Aceptar",[validators.Required()])

class NonPathologicalBackgroundForm(Form):
	defecation = TextField("Frecuencia de defecación", [validators.length(max=100)])
	toothbrushing = TextField("Frecuencia de lavado de dientes", [validators.length(max=100)])
	cigarrettes = TextField("Cigarrillos al día", [validators.length(max=100)])
	years = TextField("Años", [validators.length(max=100)])
	beverages = TextField("Bebida", [validators.length(max=100)])
	frecuency = TextField("Frecuencia", [validators.length(max=100)])
	physical_activity = TextField("Actividades", [validators.length(max=500)])
	frecuency2 = TextField("Frecuencia", [validators.length(max=100)])
	other = TextField("Otro", [validators.length(max=500)])
	submit = SubmitField("Aceptar",[validators.Required()])

class InboxForm(Form):
	doctor = IntegerField("Cédula de identidad del médico a quien se refiere el paciente", [validators.Required()])
	subject = TextField("Cuerpo del mensaje (razón de referencia y paciente a referir)", [validators.length(max=500)])
	submit = SubmitField("Enviar",[validators.Required()])

class PatientConsultationForm(Form):
	date = DateField("Fecha", [validators.Required()])
	motive = TextField("Motivo", [validators.length(max=500)])
	symptoms = TextField("Síntomas", [validators.length(max=500)])
	submit = SubmitField("Aceptar",[validators.Required()])