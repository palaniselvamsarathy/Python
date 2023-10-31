import json
# fp = open('data.json','r')

# new_dict = json.load(fp)

# for gen in new_dict:
#     print(gen['gender'])
# fp.close()

emp = {
    'eid':101,
    'ename':'sara',
    'esal' : 45000,
    'avail':True
}
fp = open('some.json','w')
json.dump(emp,fp)
fp.close()