import sqlite3

def connect():
    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS song (id INTEGER PRIMARY KEY, song TEXT, artist TEXT, album TEXT, year INTEGER)")
    conn.commit()
    conn.close()

def insert(song, artist, album, year):
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO song VALUES (NULL, ?, ?, ?, ?)", (song, artist, album, year))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM song")
    rows = cur.fetchall()
    conn.close()
    return rows

def search(song="", artist="", album="", year=""):
    conn=sqlite3.connect("songs.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM song WHERE song=? OR artist=? OR album=? OR year=?", (song, artist, album, year))
    rows = cur.fetchall()
    conn.close()
    return rows

def delete(id):
    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM song WHERE id=?", (id,)) # don't forget the comma or python will not interptret this as a tuple
    conn.commit()
    conn.close()

def update(id, song, artist, album, year):
    conn = sqlite3.connect("songs.db")
    cur = conn.cursor()
    cur.execute("UPDATE song SET song=?, artist=?, album=?, year=? WHERE id=?", (song, artist, album, year, id)) # don't forget the comma or python will not interptret this as a tuple
    conn.commit()
    conn.close()

connect()
insert("Gettin' Jiggy with it", "Will Smith", "Jiggin' with Jiggy", 2000)
insert("Takin' Care of Business", "BTO", "Some album", 1983)
#delete(1)
print(view())
print(search(artist="Will Smith"))
update(2,"Getting Jiggy with it", "Willy Smith", "Jiggin' with the oldies", 2000)
print(view())
