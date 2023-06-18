import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template('index.html')


def main():
    app.run(host="0.0.0.0", debug=False)


if __name__ == "__main__":
    main()
