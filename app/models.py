import sqlite3

def insertDataToForm(form):
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        cusor.execute(f"INSERT INTO User (username, email, image_file, password)VALUES ('{form.username.data}', '{form.email.data}', 'default.jpg', '{form.password.data}')")

def insertDataToPost(form, username):
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        userID = getNameID(username)
        cusor.execute(f"INSERT INTO Post(title, content, userID) VALUES ('{form.title.data}', '{form.contentPost.data}', {userID})")
        
def getNameList():
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        cusor.execute(f"SELECT Username FROM User")
        res = cusor.fetchall()
        return res[0]
        
def getNameID(username):
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        cusor.execute(f"SELECT userID FROM User WHERE username = '{username}'")
        res = cusor.fetchall()
        print(username)
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