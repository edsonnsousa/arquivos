f = open('words.txt','r')
cont=0.0
total=0.0

for i in f.readlines():
	if 'e' in i:
		cont+=1
	else:
		print i
	total+=1
print '%.2f %%'%(((total - cont)/total)*100.0)
	

