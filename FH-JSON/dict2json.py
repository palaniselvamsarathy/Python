import json

emp = {
    'eid': 101,
    'ename': 'sarathy', 
    'esal': 45000.0, 
    'avail': True
    }

new_obj = json.dumps(emp)

print(new_obj)