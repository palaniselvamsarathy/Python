import json

json_string_method = '''{
    "eid" : 101,
    "ename" : "sarathy",
    "esal" : 45000.00,
    "avail": true
}'''

new_obj = json.loads(json_string_method)

print(new_obj)
print(new_obj['ename'])