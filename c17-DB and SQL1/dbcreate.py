import sqlite3

sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file


# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# we can simply execute SQL using string literals as follows...
c.execute("CREATE TABLE IF NOT EXISTS person (ID 'INTEGER' PRIMARY KEY, FName 'TEXT', LName 'TEXT')")

conn.commit()
conn.close()
