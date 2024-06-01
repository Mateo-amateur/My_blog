import sqlite3

def insertDataToForm(form):
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        cusor.execute(f"INSERT INTO User (username, email, image_file, password)VALUES ('{form.username.data}', '{form.email.data}', 'default.jpg', '{form.password.data}')")
        
def getNameList():
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        cusor.execute(f"SELECT Username FROM User")
        res = cusor.fetchall()
        return res[0]

def getPassword(username):
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        cusor.execute(f"SELECT Password FROM User WHERE Username = '{username}'")
        res = cusor.fetchall()
        return res[0][0]