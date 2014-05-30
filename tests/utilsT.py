

def get_status(file_name):
	f = open(file_name, "r")
	get_status_result =  f.read()
	f.close()
	return get_status_result
