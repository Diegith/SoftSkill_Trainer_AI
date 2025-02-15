# filepath: [routes.py](http://_vscodecontentref_/4)
from flask import Blueprint, render_template, request, redirect, url_for
from .forms import ScenarioForm

main = Blueprint('main', __name__)

@main.route('/', methods=['GET', 'POST'])
def index():
    form = ScenarioForm()
    if form.validate_on_submit():
        # Aquí puedes procesar los datos del formulario
        data = {
            'nombre_escenario': form.nombre_escenario.data,
            'cliente': form.cliente.data,
            'autor': form.autor.data,
            'area_conocimiento': form.area_conocimiento.data,
            'duracion': form.duracion.data,
            'lenguaje': form.lenguaje.data,
            'descripcion_escenario': form.descripcion_escenario.data,
            'objetivo1': form.objetivo1.data,
            'objetivo2': form.objetivo2.data,
            'personajes': form.personajes.data,
            'dificultad': form.dificultad.data,
            'retroalimentacion': form.retroalimentacion.data,
            'autorizacion': form.autorizacion.data,
            'grabar': form.grabar.data,
        }
        print(data)
        # Aquí puedes enviar los datos a una API o guardarlos en una base de datos
        return redirect(url_for('main.index'))
    return render_template('index.html', form=form)