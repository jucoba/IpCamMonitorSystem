import glob
import inspect
import json

class ConfigUtils:

	def getConfigFiles(self):		
		return glob.glob("config/*.config")

		
	def getUrl(self, camera_name):
		file = self.getConfigFiles()[0]
		print file
		configFile = open(file)
		json_config = json.loads(configFile.read())
		return json_config["url"]

	def getUser(self, camera_name):
		file = self.getConfigFiles()[0]
		print file
		configFile = open(file)
		json_config = json.loads(configFile.read())
		return json_config["user"]

	def getPwd(self, camera_name):
		file = self.getConfigFiles()[0]
		print file
		configFile = open(file)
		json_config = json.loads(configFile.read())
		return json_config["password"]		