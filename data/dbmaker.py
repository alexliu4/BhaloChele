import sqlite3   #enable control of an sqlite database

DB_FILE="curbur.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

c.execute("CREATE TABLE {0} ({1} INTEGER PRIMARY KEY, {2} TEXT, {3} TEXT);".format("accounts", "account_id", "username", "password"))
c.execute("CREATE TABLE {0} ({1} INTEGER, {2} TEXT);".format("stories_viewable", "account_id", "titles"))
c.execute("CREATE TABLE {0} ({1} TEXT UNIQUE);".format("list_stories", "titles"))

#==========================================================

db.commit() #save changes
db.close() #close database
