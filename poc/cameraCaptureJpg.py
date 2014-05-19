from urllib.request import urlopen
for i in range(1,1000):
	con = urlopen("http://192.168.1.101/snapshot.cgi?user=pi&pwd=pi")
	data = con.read()
	f = open('img/camImg%s.jpg' % (i),'wb')
	f.write(data)
	f.close
	print('snap %s' % (i))
	con.close
