# app/auth/forms.py
from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo

from ..models import Funcionario


class RegistrationForm(FlaskForm):
    """
    Form for users to create new account
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    usuario = StringField('Usuario', validators=[DataRequired()])
    primeiro_nome = StringField('Primeiro nome', validators=[DataRequired()])
    ultimo_nome = StringField('Sobrenome', validators=[DataRequired()])
    senha = PasswordField('Senha', validators=[DataRequired(),EqualTo('confirmar_senha')])
    confirmar_senha = PasswordField('Confirmar senha')
    enviar = SubmitField('Registrar')

    def validate_email(self, field):
        if Funcionario.query.filter_by(email=field.data).first():
            raise ValidationError('Email ja esta em uso.')

    def validate_usuario(self, field):
        if Funcionario.query.filter_by(usuario=field.data).first():
            raise ValidationError('Nome de usuario ja esta em uso.')


class LoginForm(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Email', validators=[DataRequired(), Email()])
    senha = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')