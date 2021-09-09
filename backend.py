import sqlite3

def connect():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS books ( id INTEGER PRIMARY KEY, title TEXT, author TEXT, year INTEGER, isbn INTEGER)")
    conn.commit()
    conn.close()

def insert(title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    title = str(title).capitalize()
    author = str(author).capitalize()
    cur.execute("INSERT INTO books VALUES( NULL, ?, ?, ?, ?)",(title , author, year, isbn))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?",(id, ))
    conn.commit()
    conn.close()

def view():
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(title='', author='', year='', isbn=''):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title=? OR author=? OR year=? OR isbn=?",(title.capitalize(), author.capitalize(), year, isbn))
    rows = cur.fetchall()
    conn.close()
    return rows

def update(id, title, author, year, isbn):
    conn = sqlite3.connect("book.db")
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?",(title.capitalize() , author.capitalize(), year, isbn, id))
    conn.commit()
    conn.close()

connect()

if __name__ == '__main__':
    insert('pythons', 'guido van Rosum', 1989, 6969)
    insert('C', 'denis ritchie', 1980, 123)
    # insert("Love isn't real", "me", 2021, 420)
    print(view())