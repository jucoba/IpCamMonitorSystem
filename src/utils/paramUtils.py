
import urllib2

class ParamUtils:

	def get_status(self, url, user, pwd):
		request_url =  "http://%s/get_status.cgi?user=%s&pwd=%s"%(url, user, pwd)
		data = urllib2.urlopen(request_url).read()
		stData = data.decode()
		return parse(stData)
		        



	def parse(self, paramsStr):
		params = paramsStr.split(";")
        	striped = map(lambda x: x.strip()[4:], params)
        	dic = {}
        	for entry in striped:
                	if "=" in entry:
                        	key, val = entry.split('=')
                        	dic[key] = val.translate(None,"'")

		return dic
