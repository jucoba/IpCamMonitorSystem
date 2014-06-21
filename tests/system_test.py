import unittest
import utilsT
from camera.camera import *
from nose.tools import *
from utils.paramUtils import *
from mock import Mock

class CameraSystem(unittest.TestCase):
	paramUtil = ParamUtils()
	params = None

	

	def system_test_get_cam_alert_not_activated(self):
		url = "192.168.1.101"	
		cam = Camera(url)		
		self.assertFalse(cam.motion_detected())