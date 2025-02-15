# filepath: [run.py](http://_vscodecontentref_/5)
from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)