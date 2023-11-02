list1 = [10,20,30,2.36,'s',"Sarathy",[],(),{10},{'name':'sarathy'}]

# using indexing

print(list1[3])
print(list1[-1])

print(list1[2:4])

print()
print()
for i in list1:
    print(i)

print()
print()
j=0
while j<len(list1):
    print(list1[j])
    j+=1
