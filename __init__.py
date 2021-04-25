from flask import Flask, g, render_template

app = Flask(__name__)
app.debug = True


@app.before_request
def before_request():
    print("before request!")
    g.str = "한글"


@app.route("/gg")
def helloworld2():
    return "Hello Flask World!" + getattr(g, 'str', '111')


@app.route("/")
def helloworld():
    return render_template("index.html")


app.run(host='0.0.0.0', port='5000')
