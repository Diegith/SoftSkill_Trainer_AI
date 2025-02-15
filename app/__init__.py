# filepath: [__init__.py](http://_vscodecontentref_/2)
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    from .routes import main
    app.register_blueprint(main)

    return app