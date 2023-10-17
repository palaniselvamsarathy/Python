fp = open('data.txt', 'r+')

fp1 = fp.read()

fp2 = open('bangalore.txt','w')
fp2.write(fp1)
print(fp2)

fp2.close()
fp.close()