import sqlite3

sqlite_file = 'dbsample.sqlite'
table_name = 'Person'  # name of the table access

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.format(tn=table_name, v1=10, v2='"Bob"', v3='"Gainey"'))
c.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.format(tn=table_name, v1=11, v2='"Bobby"', v3='"Orr"'))
c.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.format(tn=table_name, v1=12, v2='"Sidney"', v3='"Crosby"'))
c.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.format(tn=table_name, v1=13, v2='"Guy"', v3='"Lafleur"'))

conn.commit()
conn.close()
