import glob
import inspect
import json

class ConfigUtils:

	json_data = None

	def getConfigFiles(self):		
		return glob.glob("config/*.config")

	def loadJsonData(self):
		file = self.getConfigFiles()[0]		
		configFile = open(file)
		self.json_data = json.loads(configFile.read())
		
	def getUrl(self, camera_name):		
		self.loadJsonData()
		return self.json_data["url"]

	def getUser(self, camera_name):
		self.loadJsonData()
		return self.json_data["user"]

	def getPwd(self, camera_name):
		self.loadJsonData()
		return self.json_data["password"]		