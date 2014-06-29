import os
import inspect

class ConfigUtils:

	def getConfigFiles(self):
		return os.listdir("./config")		
		#return ["cam2.config"]