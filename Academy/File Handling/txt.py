fp = open('data.txt','r')

data = fp.read(50)
print(data)

fp.close()
for line in data:
    print(line)