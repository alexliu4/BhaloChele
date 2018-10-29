import sqlite3   #enable control of an sqlite database

def add_account(user, pswd): #enables adding accounts
	DB_FILE="data/curbur.db"

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

def search_stories(term): #returns a list of stories with the term specified
	DB_FILE="data/curbur.db"
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

def find_id(user): #gets the account id from a username
	DB_FILE="data/curbur.db"
	db = sqlite3.connect(DB_FILE,check_same_thread=False) #open if file exists, otherwise create
	c = db.cursor()               #facilitate db ops
	c.execute("SELECT * FROM accounts")
	id = 0
	for thing in c:
		if user == thing[1]:
			id = int(thing[0])
			return id
	return -1
	db.commit() #save changes
	db.close() #close databas

def add_to_viewed_stories(acc_id, title): #records which stories have the users particpated in

	DB_FILE="data/curbur.db"
	db = sqlite3.connect(DB_FILE)
	c = db.cursor()
	c.execute("INSERT INTO {0} VALUES( {1}, '{2}');".format('stories_viewable', acc_id, title))

	db.commit() #save changes
	db.close() #close database

def add_text(user, title, text): #adds text to an existing story
	DB_FILE="data/curbur.db"
	db = sqlite3.connect(DB_FILE,check_same_thread=False) #open if file exists, otherwise create
	c = db.cursor()               #facilitate db ops

	acc_id = find_id(user)

	add_to_viewed_stories(acc_id, title)
	c.execute("SELECT entry_id FROM {0}".format(title))
	entry_id = 0
	for thing in c:
		entry_id = thing[0]
	c.execute("INSERT INTO {0} VALUES( {1}, '{2}');".format(title, entry_id+1, text))
	db.commit() #save changes
	db.close() #close database

def add_new_story(user,title,text): #adds a new story
	DB_FILE="data/curbur.db"

	db = sqlite3.connect(DB_FILE,check_same_thread=False) #open if file exists, otherwise create
	c = db.cursor()

	acc_id = find_id(user)

	add_to_viewed_stories(acc_id, title)
	c.execute("CREATE TABLE {0} ({1} INTEGER PRIMARY KEY, {2} TEXT UNIQUE);".format(title, "entry_id", "entry"))
	c.execute("INSERT INTO {0} VALUES( {1}, '{2}');".format(title, 0, text))
	c.execute("INSERT INTO {0} VALUES('{1}')".format("list_stories", title))
	db.commit() #save changes
	db.close() #close database

def get_accounts(user): #retrieves the password of the username if the account exists otherwise it returns an empty string
	DB_FILE="data/curbur.db"

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

def title_exist(title): #returns true if the title of a story is taken
	DB_FILE="data/curbur.db"

	db = sqlite3.connect(DB_FILE,check_same_thread=False) #open if file exists, otherwise create
	c = db.cursor()
	c.execute("SELECT * FROM {0}".format("list_stories"))

	for thing in c:
		if title == thing[0]:
			return True
			db.commit() #save changes
			db.close()
			return x
	db.commit() #save changes
	db.close() #close database
	return False

def viewed_stories(user): #returns all the titles that a user has viewed
	DB_FILE = "data/curbur.db"

	db = sqlite3.connect(DB_FILE,check_same_thread = False)
	c = db.cursor()
	acc_id = find_id(user)
	c.execute("SELECT * FROM {0} WHERE {1} = {2};".format("stories_viewable", "account_id", acc_id))
	d = []
	for item in c:
		d.append(item[1])
	return d
	db.commit()
	db.close()

def get_latest_update(title):# returns the last entry in a specified story
	DB_FILE = "data/curbur.db"

	db = sqlite3.connect(DB_FILE,check_same_thread = False)
	c = db.cursor()

	c.execute("SELECT {0} FROM {1}".format('entry',title))
	latest = ""
	for entry in c:
		latest = entry[0]
	return latest
	db.commit()
	db.close()

def get_added_accounts(title): #returns a list that added to a specified story
	DB_FILE = "data/curbur.db"

	db = sqlite3.connect(DB_FILE,check_same_thread = False)
	c = db.cursor()

	c.execute("SELECT {0} FROM {1} WHERE {2} = '{3}'".format('account_id', "stories_viewable", "titles", title))

	ids = []
	for thing in c:
		ids.append(thing[0])
	print(ids)
	return ids
	db.commit()
	db.close()

def whole_story(title): # returns the whole story in a string
	DB_FILE = "data/curbur.db"

	db = sqlite3.connect(DB_FILE,check_same_thread = False)
	c = db.cursor()

	c.execute("SELECT {0} FROM {1}".format("entry", title))
	text = ""
	for thing in c:
		text += thing[0] + "\n"
	print(text)
	return text
	db.commit()
	db.close()

def all_stories(user): # returns a list of all stories
	DB_FILE = "data/curbur.db"

	db = sqlite3.connect(DB_FILE,check_same_thread = False)
	c = db.cursor()
	c.execute("SELECT * FROM list_stories")
	stories = []
	for thing in c:
		stories.append(thing[0])
	return stories
	db.commit() #save changes
	db.close() #close database
