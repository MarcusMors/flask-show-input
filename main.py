from flask import Flask, request, make_response, redirect, render_template

app = Flask(__name__)

names = []


@app.route('/')
def index():
    return render_template("index.html")


# @app.route("/<string:name>")
# def session(name):
#     names.append(name)
#     context = {"names": names}
#     return render_template("index.html", **context)


@app.route("/hello", methods=["POST"])
def login():
    name = request.form.get("name")
    names.append(name)
    context = {"names": names}
    return render_template("index.html", **context)


if __name__ == '__main__':
    app.run(debug=True)
