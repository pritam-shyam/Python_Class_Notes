import sqlite3

sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file
table_name = 'Players'   # name of the table to be queried

conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

cur.execute('SELECT * FROM {tn}'.format(tn=table_name))
one_row = cur.fetchone()
print('1a):', one_row)
print(type(one_row))
all_rows = cur.fetchall()
print('1b):', all_rows)
print(type(all_rows))
conn.close()
