import sqlite3

def insertDataToForm(form):
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        try:
            cusor.execute(f"INSERT INTO User (username, email, image_file, password, theme) VALUES ('{form.username.data}', '{form.email.data}', 'default.jpg', '{form.password.data}', light)")
            return None
        except:
            return 'This username now exist'

def insertDataToPost(form, username):
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        userID = getNameID(username)
        cusor.execute(f'''INSERT INTO Post(title, content, userID) VALUES ("{form.title.data}", "{form.contentPost.data}", {userID})''')
            
def configPreferens(theme, username):
    if username == None:
        pass
    else:
        with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
            cusor = conn.cursor()
            cusor.execute(f'''UPDATE User SET theme = "{theme}" WHERE username = "{username}"''')
        
def getNameList():
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        cusor.execute(f"SELECT Username FROM User")
        res = cusor.fetchall()
        return res
        
def getNameID(username):
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        cusor.execute(f"SELECT userID FROM User WHERE username = '{username}'")
        res = cusor.fetchall()
        return res[0][0]

def getPassword(username):
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        cusor.execute(f"SELECT Password FROM User WHERE Username = '{username}'")
        res = cusor.fetchall()
        return res[0][0]
    
def getPosts():
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        cusor.execute("SELECT U.username, P.title , P.content FROM Post P INNER JOIN User U WHERE U.userID = P.userID")
        res = cusor.fetchall()
        return res

def getPreferens(username):
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        cusor.execute(f"SELECT theme FROM User WHERE Username = '{username}'")
        theme = cusor.fetchall()
        with open('entor-blog/my_blog/app/static/txt/preferences.txt', 'w', encoding='UTF-8') as pref:
            pref.write(('{"theme": "' + theme[0][0] + '"}'))

def clearPreferent():
    with open('entor-blog/my_blog/app/static/txt/preferences.txt', 'w', encoding='UTF-8') as pref:
        pref.write((''))