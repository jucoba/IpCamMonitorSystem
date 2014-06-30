import unittest
import utilsT
from camera.camera import *
from nose.tools import *
from utils.paramUtils import *
from mock import Mock
from camera.cameraManager import *

class CameraTest(unittest.TestCase):
	paramUtil = ParamUtils()
	params = None
	manager = CameraManager()

	def setUp(self):
		get_status_result =  utilsT.get_status("tests/resources/get_status.cgi")		
		self.params = self.paramUtil.parse(get_status_result)

	def test_motion_alert_activated(self):
		cam = self.manager.getCam("192.168.1.101")
		cam.get_status = Mock(return_value=self.params)
		self.assertTrue(cam.motion_detected())

	def test_motion_alert_not_activated(self):
		cam = self.manager.getCam("192.168.1.101")
		newParams = self.params
		newParams["alarm_status"] = "0"
		cam.get_status = Mock(return_value=self.params)
		self.assertFalse(cam.motion_detected())
		
