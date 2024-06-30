from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/", methods=["POST"])
def create():
    return {}


@app.route("/template")
def template():
    return render_template("index.html")


@app.route("/<int:post_id>")
def post(post_id):
    return post_id
