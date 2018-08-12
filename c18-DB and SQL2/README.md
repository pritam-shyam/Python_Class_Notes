## DB and SQL 2

In our last class, we learned how to connect to an sqlite database, create a cursor from such a connection, execute SQL statements, and commit changes and close the database.


Let's look at a modified version of our insert program that we covered last class.

Last class we had...

```python
import sqlite3

sqlite_file = 'dbsample.sqlite'
table_name = 'Players'  # name of the table access

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()
c.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.format(tn=table_name, v1=10, v2='"Bob"', v3='"Gainey"'))
c.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.format(tn=table_name, v1=11, v2='"Bobby"', v3='"Orr"'))
c.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.format(tn=table_name, v1=12, v2='"Sidney"', v3='"Crosby"'))
c.execute('INSERT INTO {tn}  VALUES ({v1}, {v2}, {v3})'.format(tn=table_name, v1=13, v2='"Guy"', v3='"Lafleur"'))

conn.commit()
conn.close()
``````


But, let's say we want to use the receive input for our database from a user.


```python
import sqlite3

sqlite_file = 'dbsample.sqlite'
table_name = 'Players'  # name of the table access

conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

print("The Greats of Hockey DB.")

fname = str(input("First Name = "))
c.executescript('SELECT * FROM {v1} WHERE fname="{v2}";'.format(v1=table_name, v2=fname))

all_rows = c.fetchall()
print('1):', all_rows)

conn.commit()
conn.close()
```

And, if a user entered the string `Robert'; DROP TABLE Students; --`  then, the input the user has given us will actually drop the table from the database.

This is an example of the problem of SQL injection...

![db_injection.png](db_injection.png)



Using the following approach will help eliminate the possibility of this happening, and execute will only execute one SQL command at a time:

```python
c.execute('SELECT * FROM {v1} WHERE fname="{v2}";'.format(v1=table_name, v2=fname))
```

Also, you can use another approach specific to SQLite in pythion for creating our SQL :

```
c.execute('SELECT * FROM ? WHERE fname=?', table_name, fname))
```


## SQLite: Continued...

When we execute a SQL command, we get back a cursor object. We can use this object to read rows one by one, in "chunks", or all at once.

### Using the cursor object (Query handling)

Here we use the fetchall() command:

```python
import sqlite3


sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file
table_name = 'Players'   # name of the table to be queried

conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

cur.execute('SELECT * FROM {tn}'.format(tn=table_name))
all_rows = cur.fetchall()
print('1):', all_rows)
print(type(all_rows))

conn.close()

```
<center><sub>[^click here for code^](slight1.py)</sub></center>
<br>
<br>

```
$ python slight1.py
1): [(10, 'Bob', 'Gainey'), (11, 'Bobby', 'Orr'), (12, 'Sidney', 'Crosby'), (13, 'Guy', 'Lafleur')]
<class 'list'>
```


Here, we fetchone(), but then a fetchall() after

```python
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

```
<center><sub>[^click here for code^](slight2.py)</sub></center>
<br>
<br>

```
$ python slight2.py
1a): (10, 'Bob', 'Gainey')
<class 'tuple'>
1b): [(11, 'Bobby', 'Orr'), (12, 'Sidney', 'Crosby'), (13, 'Guy', 'Lafleur')]
<class 'list'>
```

Here, we fetch fetchmany(), but not all, and then fetchone() until none left.

```python
import sqlite3

sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file
table_name = 'Players'   # name of the table to be queried

conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

cur.execute('SELECT * FROM {tn}'.format(tn=table_name))
many_rows = cur.fetchmany(2)
print('1a):', many_rows)
print(type(many_rows))

all_rows = cur.fetchall()
print('1b):', all_rows)
print(type(all_rows))
conn.close()


```
<center><sub>[^click here for code^](slight3.py)</sub></center>
<br>
<br>


```
$ python slight3.py
1a): [(10, 'Bob', 'Gainey'), (11, 'Bobby', 'Orr')]
<class 'list'>
1b): [(12, 'Sidney', 'Crosby'), (13, 'Guy', 'Lafleur')]
<class 'list'>
```
Alter, we can iterate through the rows, and elements of the row, as follows:

```python
import sqlite3

sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file
table_name = 'player'   # name of the table to be queried

conn = sqlite3.connect(sqlite_file)
cur = conn.cursor()

cur.execute('SELECT * FROM {tn}'.format(tn=table_name))

for row in cur:
    for elem in row:
        print(elem)

conn.close()

```
<center><sub>[^click here for code^](slight4.py)</sub></center>
<br>
<br>

```
$ python slight4.py
10
Bob
Gainey
11
Bobby
Orr
12
Sidney
Crosby
13
Guy
Lafleur
```

### Transactions

You may read about transactions, SQLite supports transactions. Transactions allow for you to group a number of insertions almost as one transaction. If you wish to do a number of transactions, and if one fails rollback all of these transactions, you'll need to use database transactions (also, set your connection object to isolation_level=None (see below), or transactions will not work)

__NOTE__: In the following code, the last insert conflicts with a record already in the database. This is a rather contrived example, but illustrates how if a set of DML statements has one bad/unexecutable statement, you can rollback the entire transaction.


```python
import sqlite3

sqlite_file = 'dbsample.sqlite'
table_name = 'player'   # name of the table to be queried

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
```
<center><sub>[^click here for code^](slight5.py)</sub></center>
<br>
<br>

### Date and Time Handling in SQLite

Date and Time Handling in SQLite. You can test these commands using DB Browser for SQLIte (and more generally, use DB Browser for SQLite to build and test your queries and database before translating it into Python sqlite3 calls)

(note1: The following sql is taken from the sqlite.org official documentation)

(note2: as mentioned in last lecture, if you work allot with SQLite, download and install http://sqlitebrowser.org/)


```SQL
--Compute the current date.
    SELECT date('now');

--Compute the last day of the current month.
    SELECT date('now','start of month','+1 month','-1 day');

--Compute the date and time given a unix timestamp 1092941466.
    SELECT datetime(1092941466, 'unixepoch');

--Compute the date and time given a unix timestamp 1092941466, and compensate for your local timezone.
    SELECT datetime(1092941466, 'unixepoch', 'localtime');

--Compute the current unix timestamp.
    SELECT strftime('%s','now');

--Compute the number of days since the signing of the US Declaration of Independence.
    SELECT julianday('now') - julianday('1776-07-04');
-- The SQLite julianday() function returns the Julian day - the number of days since noon in Greenwich on November 24, 4714 B.C

--Compute the number of seconds since a particular moment in 2004:
    SELECT strftime('%s','now') - strftime('%s','2004-01-01 02:34:56');

--Compute the date of the first Tuesday in October for the current year.
    SELECT date('now','start of year','+9 months','weekday 2');

--Compute the time since the unix epoch in seconds (like strftime('%s','now') except includes fractional part):
    SELECT (julianday('now') - 2440587.5)*86400.0;
```
<center><sub>[^click here for code^](datetime.sql)</sub></center>
<br>
<br>


For more information on Date Time handling in SQLite, see https://www.sqlite.org/lang_datefunc.html


For more on SQLite, I'd recommend https://www.sqlite.org/docs.html or a the more tutorial oriented site here http://www.tutorialspoint.com/sqlite/sqlite_primary_key.htm


Now, here is a program that creates two tables (Players and Teams) with a foreign key relationship between Players and Teams.

We then insert values into these tables

Finally, we join these tables.

```python
import sqlite3
sqlite_file = 'dbsample2.sqlite'    # name of the sqlite database file
players_table_name = 'Players'  # name of the table access
teams_table_name = 'Teams'  # name of the table access

# connect to an existing database or create a new one if an existing one is not preset
conn = sqlite3.connect(sqlite_file)

# Connecting to the database file
c = conn.cursor()

# If a players table already exists, let's drop it and create a  new one.
c.execute("DROP TABLE IF EXISTS {v1}".format(v1=players_table_name))
c.execute("DROP TABLE IF EXISTS {v1}".format(v1=teams_table_name))

c.execute("CREATE TABLE IF NOT EXISTS {tn} (ID 'INTEGER' PRIMARY KEY AUTOINCREMENT, tName 'TEXT')".format(tn=teams_table_name))
conn.commit()
c.execute("CREATE TABLE IF NOT EXISTS {tn} (ID 'INTEGER' PRIMARY KEY AUTOINCREMENT, fName 'TEXT', lName 'TEXT', TeamID INTEGER, \
     FOREIGN KEY(TeamID) REFERENCES Teams(ID))".format(tn=players_table_name))

# add teams
c.execute('INSERT INTO {tn}  VALUES ( NULL, {teamname})'.format(tn=teams_table_name,  teamname='"Bruins"'))
bruins_id = c.lastrowid

c.execute('INSERT INTO {tn}  VALUES ( NULL, {teamname})'.format(tn=teams_table_name,  teamname='"Maple Leafs"'))
leafs_id = c.lastrowid

c.execute('INSERT INTO {tn}  VALUES ( NULL, {teamname})'.format(tn=teams_table_name,  teamname='"Penguins"'))
pens_id = c.lastrowid

c.execute('INSERT INTO {tn}  VALUES ( NULL, {teamname})'.format(tn=teams_table_name,  teamname='"Canadians"'))
cdns_id = c.lastrowid

#we can simply execute SQL using string literals as follows...
c.execute('INSERT INTO {tn}  VALUES (NULL, {fName}, {lName}, {teamID})'.format(tn=players_table_name, fName='"Bob"', lName='"Gainey"', teamID=cdns_id))
c.execute('INSERT INTO {tn}  VALUES (NULL, {fName}, {lName}, {teamID})'.format(tn=players_table_name, fName='"Bobby"', lName='"Orr"', teamID=bruins_id))
c.execute('INSERT INTO {tn}  VALUES (NULL, {fName}, {lName}, {teamID})'.format(tn=players_table_name, fName='"Sidney"', lName='"Crosby"', teamID=pens_id))
c.execute('INSERT INTO {tn}  VALUES (NULL, {fName}, {lName}, {teamID})'.format(tn=players_table_name, fName='"Guy"', lName='"Lafleur"', teamID=cdns_id))

#c.execute("CREATE TABLE IF NOT EXISTS {v1} (ID 'INTEGER' PRIMARY KEY, FName 'TEXT', LName 'TEXT')".format(v1=table_name))

c.execute('SELECT fName, lName, tName FROM {playersTN} JOIN {teamsTN} ON {teamsTN}.ID = {playersTN}.ID'.format(playersTN=players_table_name, teamsTN=teams_table_name))
all_rows = c.fetchall()
print('2):', all_rows)

conn.commit()
conn.close()

```
