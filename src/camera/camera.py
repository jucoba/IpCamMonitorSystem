from utils.paramUtils import *

class Camera():
	
	url = None
	paramUtil = ParamUtils()

	def __init__(self, url):		
		self.url = url

	def motion_detected(self):
		params = self.get_status()
		alarm_status = params["alarm_status"]
		return "1" == alarm_status

	def get_status(self):
		return self.paramUtil.get_status(self.url, "user", "pwd")
		