import glob
import inspect
import json

class ConfigUtils:
	

	def getConfigFiles(self):		
		return glob.glob("config/*.config")

	def loadJsonData(self):
		file = self.getConfigFiles()[0]		
		configFile = open(file)
		self.json_data = json.loads(configFile.read())

	def getJsonData(self):
		file = self.getConfigFiles()[0]
		configFile = open(file)		
		return json.loads(configFile.read())
		
	def getUrl(self, json_data):
		return json_data["url"] 

	#def getUrl(self, camera_name):		
	#	self.loadJsonData()
	#	return self.json_data["url"]

	def getUser(self, camera_name):
		self.loadJsonData()
		return self.json_data["user"]

	def getPwd(self, camera_name):
		self.loadJsonData()
		return self.json_data["password"]

	def getJsonConfig(self):		
		return self.getJsonData()
