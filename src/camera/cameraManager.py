from camera import *
from utils.configUtils import *

class CameraManager():
	
	def getCam(self, ip):
		c = ConfigUtils()
		json_config = c.getJsonConfig()			
		camera = Camera(json_config)
		return camera