import sqlite3

sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file
table_name = 'Players'  # name of the table access

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

# we can simply execute SQL using string literals as follows...
c.execute("CREATE TABLE IF NOT EXISTS {v1} (ID 'INTEGER' PRIMARY KEY, FName 'TEXT', LName 'TEXT')".format(v1=table_name))

conn.commit()
conn.close()
