import unittest
import utilsT
from camera.camera import *
from nose.tools import *
from utils.configUtils import *

class CameraSystem(unittest.TestCase):
	paramUtil = ParamUtils()
	params = None

	configUtil = ConfigUtils()

	#@unittest.skip("skipping system tests")
	def system_test_get_cam_alert_not_activated(self):
		url = self.configUtil.getUrl("cam1")
		cam = Camera(url)		
		self.assertFalse(cam.motion_detected())

	def system_test_get_cam_alert_not_activated(self):
		url = self.configUtil.getUrl("cam1")
		cam = Camera(url)		
		self.assertFalse(cam.motion_detected())