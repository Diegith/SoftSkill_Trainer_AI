# filepath: [forms.py](http://_vscodecontentref_/3)
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField, SubmitField
from wtforms.validators import DataRequired

class ScenarioForm(FlaskForm):
    nombre_escenario = StringField('Nombre del Escenario', validators=[DataRequired()])
    cliente = StringField('Cliente', validators=[DataRequired()])
    autor = StringField('Autor(es)', validators=[DataRequired()])
    area_conocimiento = StringField('Área(s) de Conocimiento', validators=[DataRequired()])
    duracion = StringField('Duración', validators=[DataRequired()])
    lenguaje = StringField('Lenguaje', validators=[DataRequired()])
    descripcion_escenario = TextAreaField('Descripción del Escenario', validators=[DataRequired()])
    objetivo1 = StringField('Objetivo de Aprendizaje 1', validators=[DataRequired()])
    objetivo2 = StringField('Objetivo de Aprendizaje 2', validators=[DataRequired()])
    personajes = TextAreaField('Personajes Participantes', validators=[DataRequired()])
    dificultad = SelectField('Nivel de Dificultad', choices=[(str(i), f'{i}') for i in range(6)], validators=[DataRequired()])
    retroalimentacion = TextAreaField('Tipo de Retroalimentación', validators=[DataRequired()])
    autorizacion = RadioField('Autorización para Usar el Escenario', choices=[('si', 'Sí'), ('no', 'No')], validators=[DataRequired()])
    grabar = RadioField('¿Desea grabar la sesión?', choices=[('si', 'Sí'), ('no', 'No')], validators=[DataRequired()])
    submit = SubmitField('Crear Escenario')