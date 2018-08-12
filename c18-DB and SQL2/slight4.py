import sqlite3

sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file
table_name = 'Players'   # name of the table to be queried

conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

cur.execute('SELECT * FROM {tn}'.format(tn=table_name))

for row in cur:
    for elem in row:
        print(elem)

conn.close()
