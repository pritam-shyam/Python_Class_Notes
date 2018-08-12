import sqlite3


sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file
table_name = 'person'   # name of the table to be queried
id_column = 'ID'
column_2 = 'FName'
column_3 = 'LName'

# Connecting to the database file
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

c.execute('SELECT * FROM {tn}'.format(tn=table_name))
all_rows = c.fetchall()
print('1):', all_rows)

c.execute('SELECT * FROM {tn} WHERE {cn}=10'.format(tn=table_name, cn=id_column))
all_rows = c.fetchall()
print('2):', all_rows)

conn.close()
