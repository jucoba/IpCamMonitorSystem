
import urllib2

class ParamUtils:

	def get_status(self, url, user, pwd):
		request_url =  "http://%s/get_status.cgi?user=%s&pwd=%s"%(url, user, pwd)
		data = urllib2.urlopen(request_url).read()
		stData = data.decode()
		dic = self.parse(stData)
		return dic
		        



	def parse(self, paramsStr):		
		params = paramsStr.split(";")
		striped = map(lambda x: x.strip()[4:], params)
		dic_Params = dict()		
		for entry in striped:
			if "=" in entry:
				key, val = entry.split('=')
				if (val.__class__.__name__ == "str"):
					dic_Params[key] = val.translate(None,"'")
				else:
					dic_Params[key] = val		
		print dic_Params			
		return dic_Params