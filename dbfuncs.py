import sqlite3   #enable control of an sqlite database

DB_FILE="curbur.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops

#==========================================================
#INSERT YOUR POPULATE CODE IN THIS ZONE

def add_account(user, pswd):
	DB_FILE="curbur.db"

	db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
	c = db.cursor()               #facilitate db ops

	c.execute("SELECT * FROM accounts")
	id = 0
	for thing in c:
		if user == thing[1]:
			db.commit() #save changes
			db.close() #close database
			return False
		id = thing[0]
	c.execute("INSERT INTO {0} VALUES( {1}, '{2}', '{3}');".format("accounts", int(id)+1, user, pswd))
	db.commit() #save changes
	db.close() #close database
	return True

def search_stories(term):
	DB_FILE="curbur.db"
	db = sqlite3.connect(DB_FILE)
	c = db.cursor()

	c.execute("SELECT * FROM list_stories")
	stories = []
	for thing in c:
		if term.lower() in thing[0].lower():
			stories.append(thing[0])
	return stories
	db.commit() #save changes
	db.close() #close database

def find_id(user):
	DB_FILE="curbur.db"
	db = sqlite3.connect(DB_FILE,check_same_thread=False) #open if file exists, otherwise create
	c = db.cursor()               #facilitate db ops
	c.execute("SELECT * FROM accounts")
	id = 0
	for thing in c:
		if user == thing[1]:
			id = int(thing[0])
			return id
	return 0
	db.commit() #save changes
	db.close() #close databas

def add_to_viewed_stories(acc_id, title):
	DB_FILE="curbur.db"
	db = sqlite3.connect(DB_FILE)
	c = db.cursor()
	c.execute("INSERT INTO {0} VALUES( {1}, '{2}');".format('stories_viewable', acc_id, title))

	db.commit() #save changes
	db.close() #close database

def add_text(user, title, text):
	DB_FILE="curbur.db"
	db = sqlite3.connect(DB_FILE,check_same_thread=False) #open if file exists, otherwise create
	c = db.cursor()               #facilitate db ops

	acc_id = find_id(user)

	add_to_viewed_stories(acc_id, title)
	c.execute("SELECT entry_id FROM {0}".format(title))
	entry_id = 0
	for thing in c:
		id = thing[0]
	c.execute("INSERT INTO {0} VALUES( {1}, '{2}');".format(title, entry_id+1, text))
	db.commit() #save changes
	db.close() #close database

def add_new_story(user,title,text):
	DB_FILE="curbur.db"

	db = sqlite3.connect(DB_FILE,check_same_thread=False) #open if file exists, otherwise create
	c = db.cursor()

	acc_id = find_id(user)

	add_to_viewed_stories(acc_id, title)
	c.execute("CREATE TABLE {0} ({1} INTEGER PRIMARY KEY, {2} TEXT UNIQUE);".format(title, "entry_id", "entry"))
	c.execute("INSERT INTO {0} VALUES( {1}, '{2}');".format(title, 0, text))
	c.execute("INSERT INTO {0} VALUES('{1}')".format("list_stories", title))
	db.commit() #save changes
	db.close() #close database

def get_accounts(user):
	DB_FILE="curbur.db"

	db = sqlite3.connect(DB_FILE,check_same_thread=False) #open if file exists, otherwise create
	c = db.cursor()
	c.execute("SELECT * FROM {0}".format("accounts"))

	for thing in c:
		if user == thing[1]:
			x = thing[2]
			db.commit() #save changes
			db.close()
			return x
	db.commit() #save changes
	db.close() #close database
	return ""

print(get_accounts("asdsdaaaasdasdsd"))

#add_account('a', 'a')
#add_account('b','b')
#add_new_story(0, 'story1', 'blah blah blah.')
#add_text(1, 'story1', 'halb halb halb.')
#==========================================================

db.commit() #save changes
db.close() #close database
