import sqlite3
from backend01 import *

def insert(title, artist, album, year):
    conn=sqlite3.connect(DBASE_FILE)
    cur=conn.cursor()
    cur.execute("INSERT INTO song VALUES (NULL, ?, ?, ?, ?)", (title, artist, album, year))
    conn.commit()
    conn.close()

def delete(id):
    conn = sqlite3.connect(DBASE_FILE)
    cur = conn.cursor()
    cur.execute("DELETE FROM song WHERE id=?", (id,)) # don't forget the comma or python will not interptret this as a tuple
    conn.commit()
    conn.close()

def update(id, title, artist, album, year):
    conn = sqlite3.connect(DBASE_FILE)
    cur = conn.cursor()
    cur.execute("UPDATE song SET title=?, artist=?, album=?, year=? WHERE id=?", (title, artist, album, year, id)) # don't forget the comma or python will not interptret this as a tuple
    conn.commit()
    conn.close()

def search(title="", artist="", album="", year=""):
    conn=sqlite3.connect(DBASE_FILE)
    cur=conn.cursor()
    cur.execute("SELECT * FROM song WHERE title=? OR artist=? OR album=? OR year=?", (title, artist, album, year))
    rows = cur.fetchall()
    conn.close()
    return rows


if __name__ == "__main__":
    connect()
    insert("Gettin' Jiggy with it", "Will Smith", "Big Willie", 1997)
    print(view())
    done = False
    while not done:
        choice = input("\n\nDo you want to delete or update a record? [D,U,Q]: ")
        if choice in "D":
            record_id = int(input("Enter record ID to delete (-1 to quit): "))
            if record_id > 0:
                delete(record_id)
            else:
                done = True
            print(view())
        elif choice in "U":
            record_id = int(input("OK, which record would you like to update? (-1 to quit) : "))
            if record_id > 0:
                update(record_id, "CCCCCC", "DDDDDD", "EEEEEEE", 2000)
            else:
                done = True
            print(view())
        else:
            done = True
