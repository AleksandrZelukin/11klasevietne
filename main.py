from flask import Flask,url_for, render_template,request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    return render_template("kontakt.html")

@app.route('/noteikumi')
def noteikumi():
    return render_template("noteikumi.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
