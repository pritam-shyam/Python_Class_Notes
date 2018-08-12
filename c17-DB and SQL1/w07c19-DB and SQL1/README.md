
# W07c19 SQLLite

## Intro

>SQLite is a high-reliability, embedded, zero-configuration, public-domain, SQL database engine. SQLite is the most used database engine in the world. [more info](https://www.sqlite.org/about.html)

SQLite is a complete database that is lightweight, serverless, and supports much of the SQL language. It's a great tool to apply when your programs need to store and retrieve local data using SQL.

How SQLite achieves this with such a simple approach is quite impressive.

Though SQLite can easily handle many processes (or threads) accessing the database at the same time, care must be taken when multiple updates are occurring. Only one process can update the database at any moment in time. Most updates only lock the database for a very brief time, but in large multi-user environments that can become a problem. When faced with projects that require heavy multi-user usage, SQLlite will not be the best choice. Under such conditions, we would look for a server based database system such as MySQL, PostgreSQL, Oracle, SQLserver, etc.

For a longer discussion about advantages and limitations of SQLite, please refer to the following link.
URL=http://www.sqlite.org/whentouse.html

* to understand more about locking, contention, journaling etc. see https://www.sqlite.org/lockingv3.html
* if you run into problems (or want to avoid doing so) when accessing an SQLite database (either concurrently, or not) see https://www.sqlite.org/howtocorrupt.html

But, with that said, the are many useful applications for SQLite, and often, the requirement for a large database server can be the exception rather than the rule.


## Tutorial

### Our first SQLite database: Creating structure

Let's create a simple database with one table and three columns

```python
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

```
<center><sub>[^click here for code^](dbcreate.py)</sub></center>
<br>
<br>

Let's look at what is happening here.

First, we need to import sqlite3. This is the library that provides all the code we need to create, modify, and query sqlite databases.

With the library now imported, we must create a connection to the database - `conn = sqlite3.connect(sqlite_file)`. Databases in SQLite are simply files, therefore, the parameter here is simply a pointer to a local file. If the database does not exist, it will be initialized as a blank database. If the database does already exist, it will be "connected" to and any data within the database is ready to be queried or altered.

Once connected to our new, or existing, database file we must now create a database c ursor - `c = conn.cursor()`. A cursor allows us to maintain a session with the databased where we can alter, update, and query any tables and data found within our database.

In the example above we use the cursor to create a new database table. Here we use the execute command `c.execute("some sql goes here")` to create a new table called players that consists of two fields with a atomic primary key. Creating a table does yet add any data. Table creation simple creates a structure of attributes and associated datatypes that describe an entity - in this case, the entity is a "player" and the attributes of each player we will enter are FName and LName. The player ID serves as a unique identify for each of the players we will enter in the system.

Finally, if we have made any alterations to the database (which, in this case, we most definitely have) we need to ensure we commit these changes by calling the commit method of our database connection - `conn.commit()` and then close the connection - `conn.close()`.


### Getting more "dynamic": Adding data

Things get a little more interesting when we programatically (dynamically) create  SQL statements.

In the following snippet of code, we begin to populate our players table (created in the section above) with data about individual players.

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

```

<center><sub>[^click here for code^](dbinsert.py)</sub></center>
<br>
<br>

In the above code, we find much of the same pattern as in our first example. We create a connection to our database using `sqlite2.connect(filename)`, create a cursor for the connection - ` c = conn.cursor()`, execute commands on the database - `c.connect('SOME SQL HERE')`. and commit and close the database - `conn.commit()` and `conn.close()`.

The difference with the above code is that we are inserting actual values, details, about each of the players (entities). We do this using SQL, and specifically the INSERT statement.


NOTE: There are a few different approaches on how we can insert data into our database. We will discuss other approaches (and the issue of "database injection") in later classes.

### What in there? Querying our data

Finally, we want to extract data from the database:

```python
import sqlite3


sqlite_file = 'dbsample.sqlite'    # name of the sqlite database file
table_name = 'Players'   # name of the table to be queried
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

```
<center><sub>[^click here for code^](dbquery.py)</sub></center>
<br>
<br>


The above code illustrated how we can create SQLcode for execution, and analyze the results.


### SQLite and SQL

Though there are SQL standard,

Though SQL became a standard of the American National Standards Institute (ANSI) in 1986 (and the International Organization for Standardization (ISO) in 1987), most SQL code is not completely portable among different database systems without adjustments. Each database platform has introduced additional features to SQL... but, in general the basic core functions will be portable across different databases.

Details on the SQL language supports by SQLite can be found here https://www.sqlite.org/lang.html

Other basic SQL patterns that will be portable across platforms include:

```
# Add a columns to players
ALTER TABLE players ADD COLUMN points INTEGER

# Insert a new row into players
INSERT INTO players VALUES (99, "Wayne", "Gretzky")

# Insert if it can...
INSERT OR IGNORE INTO players VALUES (10,"Bob","Gainey")

# Update existing row
UPDATE players SET ID=3 WHERE ID=10
```

Here is an overview of the datatypes supports by SQLite
```
    INTEGER: A signed integer up to 8 bytes depending on the magnitude of the value.
    REAL: An 8-byte floating point value.
    TEXT: A text string, typically UTF-8 encoded (depending on the database encoding).
    BLOB: A blob of data (binary large object) for storing binary data.
    NULL: A NULL value, represents missing data or an empty cell.
```
__NOTE__: Though many of you have experience with SQL, it is not a re-requisite for this course to have taken the database course. Therefore, my expectations surrounding your SQL ability will be to only know the basics of creating, altering, and querying tables. From today's tutorial, be sure to understand the CREATE, INSERT, and basic SELECT sql syntax and the basic SQLite datatypes.  In future classes we will cover transaction control, ALTER, UPDATE and how to join tables, drop them, and how primary and foreign key constraints work.

__NOTE__: A handy tool for exploring SQLlite DB's can be found here http://sqlitebrowser.org/
