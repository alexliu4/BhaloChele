import os

from flask import Flask, render_template, redirect, session, flash, request, url_for
app = Flask(__name__)

app.secret_key = os.urandom(32) #generate random key to use session for cookies

users = {'sh':'hi'}

@app.route("/")
def home():
    if 'sh' in session: #if a user is logged in
        return render_template("homepage.html", user = 'sh')#send to welcome page
    else:
        return render_template("login.html")#login page

@app.route("/auth", methods = ['POST'])
def login():
    if request.form['username'] in users and request.form['password'] == users[request.form['username']]:
        session['sh'] = 'hi' #logs in user
        return redirect(url_for('home'))#send to welcome page
    else:
        flash("invalid username/password. Please try again. If you do not have an account please register")
        return redirect(url_for("login"))

@app.route("/logout", methods = ["POST", "GET"])
def gohome():
	session.pop('sh',None)#logs out user. None used if no users are logged in
	return redirect(url_for('home'))#Send to login page


    
@app.route("/register")
def register():
    return 'lol'

if __name__ == "__main__":
    app.debug = True
    app.run()

