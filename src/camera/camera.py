from utils.paramUtils import *
from utils.configUtils import *

class Camera():
	
	json_data = None
	paramUtil = ParamUtils()
	configUtil = ConfigUtils()

	def __init__(self, json_data):
		self.json_data = json_data				
		self.url = self.configUtil.getUrl2(json_data)

	def motion_detected(self):
		params = self.get_status()		
		alarm_status = params["alarm_status"]
		return "1" == alarm_status

	def get_status(self):
		dic = self.paramUtil.get_status(self.url, "user", "pwd")		
		return dic

	def getUrl(self):
		return "192.168.1.101:8080"
		