import os
from flask import Blueprint, render_template, request, redirect, url_for, current_app
from .forms import ScenarioForm
from sklearn.feature_extraction.text import CountVectorizer
from openai import OpenAI

main = Blueprint('main', __name__)

def get_form_data(form):
    data = {
        'nombre_escenario': form.nombre_escenario.data,
        'cliente': form.cliente.data,
        'autor': form.autor.data,
        'area_conocimiento': form.area_conocimiento.data,
        'duracion': form.duracion.data,
        'lenguaje': form.lenguaje.data,
        'avatarAnfitrion': form.avatarAnfitrion.data,
        'rolParticipante': form.rolParticipante.data,
        'descripcion_escenario': form.descripcion_escenario.data,
        'objetivo1': form.objetivo1.data,
        'objetivo2': form.objetivo2.data,
        'contenido': form.contenido.data,
        'escenario1': form.escenario1.data,
        'escenario2': form.escenario2.data,
        'sobreLaSimulacion': form.sobreLaSimulacion.data,
        'personajes': form.personajes.data,
        'dificultad': form.dificultad.data,
        'retroalimentacion': form.retroalimentacion.data,
    }
    # print(data)
    return data

@main.route('/', methods=['GET', 'POST'])
def index():
    form = ScenarioForm()
    if form.validate_on_submit():
        data = get_form_data(form)
        # print(data)
        # Aquí puedes enviar los datos a una API o guardarlos en una base de datos
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form)


@main.route('/openai', methods=['POST'])
def openai_api():
    form = ScenarioForm()
    if form.validate_on_submit():
        data = get_form_data(form)
        client = OpenAI(
            base_url=current_app.config['OPENAI_BASE_URL'],
            api_key=current_app.config['OPENAI_API_KEY'],
        )

        response = client.chat.completions.create(
            model="deepseek/deepseek-r1",
            messages=[
                {
                    "role": "system",
                    "content": "You are an AI assistant who knows everything, designed to solve practical cases for the development of soft skills related to different contexts and professional areas.",
                },
                {
                    "role": "user",
                    "content": f"Propose some of the possible alternatives in which I might be exposed in a real practical scenario, including responses and questions, given the conditions provided in the data: {data}",
                },
            ],
        )

        message = response.choices[0].message.content
        print(f"Assistant: {message}")
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form)
