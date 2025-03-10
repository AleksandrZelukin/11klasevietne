from flask import Flask, request, render_template, redirect,flash,url_for
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
app = Flask(__name__)

db = sqlite3.connect('login_password.db')
sql = db.cursor()

sql.execute('''CREATE TABLE IF NOT EXISTS passwords(
id_user INTEGER PRIMARY KEY AUTOINCREMENT,
login TEXT,
parole TEXT);''')

db.commit()
sql.close()
db.close()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/hello')
def hello():
    return render_template("kontakt.html")

@app.route('/noteikumi')
def noteikumi():
    return render_template("noteikumi.html")

@app.route('/login', methods=['GET', 'POST'])
def autorizacija():
    if request.method == 'POST':
        login = request.form.get('login')
        parole = request.form.get('parole')
        db = sqlite3.connect('login_password.db')
        sql = db.cursor()
        info = sql.execute(("""SELECT login from passwords WHERE login = '{}'""").format(login)).fetchone()
        if info in None:
            return "Password nekorekts!"
# def login():
#     return render_template("login.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5050)
