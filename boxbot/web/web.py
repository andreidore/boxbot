import flask
from reactpy import component, html
from reactpy.backend.flask import configure

app = flask.Flask(__name__)


@component
def HelloWorld():
    return html.h1("Hello, world!")


app = flask.Flask(__name__)
configure(app, HelloWorld)

if __name__ == "__main__":
    app.run(debug=True)
