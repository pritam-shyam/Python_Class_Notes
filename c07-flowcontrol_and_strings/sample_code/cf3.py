passwords = {'Tim': 'sdfasdf', 'Bob': 'dfafsdc', 'Sue': 'wnkrewd'}
uname = input('Please enter your username : ')
username, password = uname, passwords.get(uname, 'unkown')
print(username,password)
