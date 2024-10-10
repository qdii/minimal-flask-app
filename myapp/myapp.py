from flask import Flask
from gunicorn.app.wsgiapp import run

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World!"


if __name__ == "__main__":
    run()
