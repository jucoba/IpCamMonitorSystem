from urllib.request import urlopen 
from time import sleep

while True:
	data = urlopen("http://192.168.1.101:81/get_status.cgi?user=pi&pwd=pi").read()
	stData = data.decode()
	params = stData.split(";")
	striped = map(lambda x: x.strip()[4:], params)
	dic = {}
	for entry in striped:
		if "=" in entry:
        		key, val = entry.split('=')
        		dic[key] = val

	print(dic["alarm_status"])
	sleep(1)
