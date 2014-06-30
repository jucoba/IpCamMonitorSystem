from camera import *
from utils.configUtils import *

class CameraManager():

	camera_list = {}
	config = ConfigUtils()

	def loadcameras(self):
		camera_data_list = self.config.getCamConfigList()
		for key, value in camera_data_list.iteritems():
			self.camera_list[key] = Camera(value)			
		return self.camera_list

	
	def getCam(self, ip):
		if ip not in self.camera_list:
			self.loadcameras()

		return self.camera_list[ip]