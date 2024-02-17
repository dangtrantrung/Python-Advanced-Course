import json  # same as python dictionary obj

dict={
    'name':"Trung",
    'age': 40,
    'hobbies': ['sleeping','ping pong', 'dev', 'eating']
    }

# convert python dict to JSON string
json_string=json.dumps(dict)
print(type(json_string))
print(json_string)
# convert json string to python object
new_dict=json.loads(json_string)
print(type(new_dict))
print(new_dict)
print(new_dict['hobbies'])
for hb in new_dict['hobbies']:
    print(hb)

    assert dict==new_dict
    print('test assert ok')

with open('save.json','w') as f:
    json.dump()