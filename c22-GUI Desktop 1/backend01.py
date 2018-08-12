import sqlite3

DBASE_FILE = 'dbase/songs.db'

def connect():
    conn = sqlite3.connect("dbase/songs.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS song (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, artist TEXT, album TEXT, year INTEGER)")
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect(DBASE_FILE)
    cur=conn.cursor()
    cur.execute("SELECT * FROM song")
    rows = cur.fetchall()
    conn.close()
    return rows

if __name__ == "__main__":
    connect()
    print(view())
