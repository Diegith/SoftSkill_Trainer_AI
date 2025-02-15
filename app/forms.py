from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, RadioField, SubmitField
from wtforms.validators import DataRequired

choices = {
    'roles': [('Administrativo', 'Administrativo'), ('Consejero', 'Consejero'), ('Contador', 'Contador'), ('Directivo','Directivo'), ('Diseñador', 'Diseñador'), ('Docente', 'Docente'), ('Ingeniero', 'Ingeniero'), ('Medico tratante', 'Medico tratante'), ('Par', 'Par'), ('Secretaria', 'Secretaria'), ('Servicio al cliente', 'Servicio al cliente')]
}

class ScenarioForm(FlaskForm):

    # Seccion 0: Datos Iniciales
    nombre_escenario = StringField('Nombre del Escenario', validators=[DataRequired()])
    cliente = StringField('Cliente', validators=[DataRequired()])
    autor = StringField('Autor(es)', validators=[DataRequired()])
    area_conocimiento = StringField('Área(s) de Conocimiento', validators=[DataRequired()])
    duracion = SelectField('Duración (minutos)', choices=[(str(i), f'{i}') for i in range(5,25)], validators=[DataRequired()])
    lenguaje = SelectField('Lenguaje', choices=[('es', 'Español'), ('en', 'Inglés')], validators=[DataRequired()])
    avatarAnfitrion = SelectField('Avatar Anfitrion', choices=[('no', 'No'), ('si', 'Sí')], validators=[DataRequired()])
    
    # Seccion 1: El parcipante
    rolParticipante = SelectField('Rol Participante', choices=choices['roles'], validators=[DataRequired()])
    descripcion_escenario = TextAreaField('Descripción del Escenario', validators=[DataRequired()])
    objetivo1 = StringField('Objetivo de Aprendizaje 1', validators=[DataRequired()])
    objetivo2 = StringField('Objetivo de Aprendizaje 2', validators=[DataRequired()])
    
    # Seccion 2: El contenido  
    contenido = TextAreaField('Contenido', validators=[DataRequired()])
    
    # Seccion 3: El Escenario  
    escenario1 = StringField('Escenario 1', validators=[DataRequired()])
    escenario2 = StringField('Escenario 2', validators=[DataRequired()])
    sobreLaSimulacion = StringField('Sobre la simulación', validators=[DataRequired()])

    # Seccion 4: Los personajes
    personajes = SelectField('Personajes de la simulación', choices=[('Adultos', 'Adultos'), ('Niños/Jóvenes', 'Niños/Jóvenes')], validators=[DataRequired()])
    dificultad = SelectField('Nivel de Dificultad', choices=[(str(i), f'{i}') for i in range(6)], validators=[DataRequired()])

    # Seccion 5: La retroalimentación
    retroalimentacion = TextAreaField('Tipo de Retroalimentación', validators=[DataRequired()])
    
    submit = SubmitField('Crear Escenario')