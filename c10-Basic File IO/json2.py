import json
somedata = [{'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4), 'b': 3.0}]
with open('data01.json','w') as outfile:
  json.dump(somedata, outfile)
