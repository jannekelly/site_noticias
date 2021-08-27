# app/admin/forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class NoticiaFormulario(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    titulo = StringField('Titulo', validators=[DataRequired()])
    caminho_imagem = StringField('Imagem', validators=[DataRequired()])
    texto = TextAreaField('Texto', validators=[DataRequired()])
    submit = SubmitField('Submit')

class FuncionarioFormulario(FlaskForm):
    """
    Form for admin to add or edit a department
    """
    email = StringField('Email', validators=[DataRequired()])
    usuario = StringField('Usuario', validators=[DataRequired()])
    primeiro_nome = StringField('Primeiro nome', validators=[DataRequired()])
    ultimo_nome = StringField('Sobrenome', validators=[DataRequired()])
    submit = SubmitField('Submit')
