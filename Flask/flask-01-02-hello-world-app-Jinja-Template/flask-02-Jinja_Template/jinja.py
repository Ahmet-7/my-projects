from flask import Flask, render_template

app = Flask(__name__)



@app.route("/")
def head():
    return render_template("index.html", number1=1234, number2=7896)

@app.route("/mult")
def number():
    num1 = 23
    num2 = 54
    return render_template("body.html", value1=num1, value2=num2, mult=num1*num2)



if __name__== "__main__":
    app.run(debug=True)