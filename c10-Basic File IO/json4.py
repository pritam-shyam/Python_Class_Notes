import json
somedata = {'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4),
            'b': 3.0, 'c': {'x': 12, 'y': 100}}
print('ORIGINAL: ', somedata)

f = open('data.json', 'w')
json.dump(somedata, f)
f.close()

f = open('data.json', 'r')
somedata = json.load(f)
f.close()
print('READ FROM JSON FILE: ', somedata)

somedata['fname'] = 'Al'
f = open('data.json', 'w')
json.dump(somedata, f)
f.close()
print('EDITED IN MEMORY: ', somedata)

f = open('data.json', 'w')
json.dump(somedata, f)
f.close()

f = open('data.json', 'r')
somedata = json.load(f)
f.close()
print('RE-READ FROM JSON: ', somedata)
