from flask import Flask 

app = Flask(__name__)

@app.route("/")
def head():
    return "<h1>Ahmed Tugrul Bayrak</h1>"


@app.route("/second")
def second():
    return "<h1>This is my second page</h1>"

@app.route("/third/subthird")
def third():
    return "<h2>This is the subpath of third page</h2>"

@app.route("/forth/<string:id>")
def forth(id):
    return f'Id number of this page is {id}'


if __name__ == "__main__":
    app.run(debug=True)