f = open('words.txt','r')
for i in f.readlines():
	if len(i) >=20:
		print i
