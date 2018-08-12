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
