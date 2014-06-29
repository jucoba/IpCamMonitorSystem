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
		#return "192.168.1.101:8080"