import os, sqlite3
import dbfuncs as dbfuncs
from flask import Flask, render_template, redirect, session, flash, request, url_for
app = Flask(__name__)

app.secret_key = os.urandom(32) #generate random key to use session for cookies

users = {'sh':'hi'}



@app.route("/")
def home():
    if 'logged_in?' in session and session['logged_in?']: #if a user is logged in
        print(session['username'])

        return render_template("homepage.html",
                                    user = session['username'],
                                    stories = dbfuncs.viewed_stories(session['username']) )#send to welcome page
    else:
        return render_template("login.html" )#login page


@app.route("/auth", methods = ['POST'])
def login():
    wow = dbfuncs.get_accounts(request.form['username'])
    if len(wow) > 0 and wow == request.form['password']:
        session['username'] = request.form['username']
        session["logged_in?"] = True
        
        return render_template('homepage.html',
                                user = session['username'],
                                stories = dbfuncs.viewed_stories(session['username']) )#send to welcome page
    else:
        flash("Invalid username/password. Please try again. If you do not have an account please register")
        return render_template("login.html",name = request.form['username'])




    #if request.form['username'] in users and request.form['password'] == users[request.form['username']]:
    #    session['sh'] = 'hi' #logs in user
    #    return render_template('homepage.html')#send to welcome page
    #else:
    #    flash("Invalid username/password. Please try again. If you do not have an account please register")
    #    return render_template("login.html")

@app.route("/logout", methods = ["POST", "GET"])
def gohome():
    session.pop('username',None)#logs out user. None used if no users are logged in
    session["logged_in?"] = False
    return redirect(url_for('home'))#Send to login page


@app.route("/register", methods = ['POST'])
def register():
	if not dbfuncs.add_account(request.form['rusername'],request.form['rpassword']): #checks is username is taken
		flash("username is taken, please try again")
		return render_template('login.html')#back to login page
	flash("registration complete. Please log in")
	return render_template('login.html')#sends back to login page

@app.route("/registerGo", methods = ['POST'])
def go():
	return render_template("register.html")


@app.route("/addStory", methods = ['POST','GET'])
def sendStoryPage():
    if 'logged_in?' in session:
        return render_template("add.html")
    else:
        flash("YOU ARE NOT LOGGED IN ANGER!!!!!")
        return redirect(url_for('home'))


@app.route("/peeppee", methods = ['POST'])
def addStory():
	dbfuncs.add_new_story(session['username'],request.form['title'], request.form['content'])
    #add request.form['title']
    #add request.form['content']
	return redirect(url_for('home'))#Send to homepage


@app.route("/viewStory", methods = ['POST'])
def view():
	s_title = request.form['title']
	ids = db.funcs.get_added_accounts(s_title)
	user_id = dbfuncs.find_id(session['username'])
	for id in ids:
		if user_id == id:
			return render_template("story.html", title = s_title, text = "the whole story")
		
	
	latesst_entry= dbfuncs.get_latest_update(s_title)
	return render_template("story.html", title = s_title, text= latest_entry[0])
	
	

if __name__ == "__main__":
    app.debug = True
    app.run()
