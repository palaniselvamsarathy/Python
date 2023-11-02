list1 = [10,20,30,2.36,'s',"Sarathy",[],(),{10},{'name':'sarathy'}]

list1.append(10)
list1.append(5)


print(list1)

list1.insert(2,12)
print(list1)

a = [10,20,40,3.5]
b=[10,24,51,36]

a.extend(b)
print(a)