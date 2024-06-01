import sqlite3

def insertDataToForm(form):
    with sqlite3.connect('entor-blog/my_blog/app/site.db') as conn:
        cusor = conn.cursor()
        cusor.execute(f"INSERT INTO User (username, email, image_file, password)VALUES ('{form.username.data}', '{form.email.data}', 'default.jpg', '{form.password.data}')")