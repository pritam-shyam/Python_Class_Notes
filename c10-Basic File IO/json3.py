import json

somedata = [{'fname': 'Alfred', 'occupation': 'Butler', 'a': (2, 4),
            'b': 3.0, 'c': {'x': 12, 'y': 100}}]

data_string = json.dumps(somedata) # translate this data struct into a json string
print('ENCODED:', data_string) # json encoded (serialized) string representation

decoded = json.loads(data_string) # reverse the process by deserializing the data.
print('DECODED:', decoded)

# now, let's compare the results of the preencoded data, and the end result of the unencoded (deserialized data)
print('ORIGINAL:', type(somedata))
print('DECODED :', type(decoded))
print('ORIGINAL:', type(somedata[0]['fname']))
print('DECODED :', type(decoded[0]['fname']))
print('ORIGINAL:', type(somedata[0]['occupation']))
print('DECODED :', type(decoded[0]['occupation']))
print('ORIGINAL:', type(somedata[0]['a']))
print('DECODED :', type(decoded[0]['a']))
print('ORIGINAL:', type(somedata[0]['b']))
print('DECODED :', type(decoded[0]['b']))
print('ORIGINAL:', type(somedata[0]['c']))
print('DECODED :', type(decoded[0]['c']))
