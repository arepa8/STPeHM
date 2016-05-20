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



class LoginForm(Form):
    username = TextField('Username', [validators.Required()])
    password = PasswordField('Password', [validators.Required()])

    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None

    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.check_password(self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True

