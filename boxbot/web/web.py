import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "sasasas"


def main():
    app.run(debug=False)


if __name__ == "__main__":
    main()
