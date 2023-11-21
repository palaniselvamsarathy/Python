fp = open('data.txt','r+')

com = fp.readline()

con = fp.write("Sarathy")
con2 = fp.writelines(["Sarathy","Sara"])

print(com)

fp.close()