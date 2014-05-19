

class ParamUtils:

	def parse(paramsStr,a):
		params = a.split(";")
        	striped = map(lambda x: x.strip()[4:], params)
        	dic = {}
        	for entry in striped:
                	if "=" in entry:
                        	key, val = entry.split('=')
                        	dic[key] = val

		return dic
