import unittest
import utilsT
from camera.camera import *
from nose.tools import *
from utils.paramUtils import *

class CameraSystem(unittest.TestCase):
	paramUtil = ParamUtils()
	params = None

	

	#@unittest.skip("skipping system tests")
	def system_test_get_cam_alert_not_activated(self):
		url = "192.168.1.101:8080"	
		cam = Camera(url)		
		self.assertFalse(cam.motion_detected())

	def system_test_get_cam_alert_not_activated(self):
		url = "192.168.1.101:8080"	
		cam = Camera(url)		
		self.assertFalse(cam.motion_detected())