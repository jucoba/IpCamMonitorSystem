import glob
import inspect

class ConfigUtils:

	def getConfigFiles(self):
		print glob.glob("config/*.config")
		return glob.glob("config/*.config")