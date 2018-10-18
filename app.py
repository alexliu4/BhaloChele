import os

from flask import Flask, render_template, redirect, session, flash
app = Flask(__name__)

app.secret_key = os.urandom(32) #generate random key to use session for cookies

user = 'shin'
passwd = 'bangla'

@app.route("/")
def home():
    if 'shin' in session: #if a user is logged in
        return render_template("homepage.html", user = 'shin')#send to welcome page
    else:
        return render_template("login.html")#send to login page

@app.route("/auth", methods = ['POST'])
def login():
    if request.form['username'] == user and request.form['password'] == passwd:
        session[request.form['username']] = request.form['password'] #logs in user
        return redirect(url_for('home'))#send to welcome page
    else:
        flash("invalid username/password. Please try again. If you do not have an account please register")
        return redirect(url_for("login"))

@app.route("/register")
def register():
    
