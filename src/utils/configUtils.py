import glob
import inspect
import json

class ConfigUtils:
	

	def getConfigFiles(self):		
		return glob.glob("config/*.config")

	def getCamConfigList(self):
		configFiles = self.getConfigFiles()
		camDict = {}
		for camConfig in configFiles:
			configData = open(camConfig)
			json_data = json.loads(configData.read())
			camDict[self.parseUrl(json_data["url"])] = json_data
		return camDict


	def parseUrl(self, url):
		ip = url.split(":")[0]
		return ip

			

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
	

	def getUser(self, camera_name):
		self.loadJsonData()
		return self.json_data["user"]

	def getPwd(self, camera_name):
		self.loadJsonData()
		return self.json_data["password"]

	def getJsonConfig(self):		
		return self.getJsonData()
