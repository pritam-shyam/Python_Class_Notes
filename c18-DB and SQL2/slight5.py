import sqlite3

sqlite_file = 'dbsample.sqlite'
table_name = 'Players'   # name of the table to be queried

conn = sqlite3.connect(sqlite_file)
conn.isolation_level = None

try:
    cur = conn.cursor()
    cur.execute("begin")
    cur.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.\
        format(tn=table_name, v1=15, v2='"Tim"', v3='"Horton"'))
    cur.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.\
        format(tn=table_name, v1=16, v2='"Wendel"', v3='"Clark"'))
    cur.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.\
        format(tn=table_name, v1=17, v2='"Ty"', v3='"Domi"'))
    cur.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.\
        format(tn=table_name, v1=11, v2='"Bobby"', v3='"Orr"'))
    cur.exectute("commit")
except:
    cur.execute("rollback")
