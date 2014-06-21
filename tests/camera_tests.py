import unittest
import utilsT
from camera.camera import *
from nose.tools import *
from utils.paramUtils import *
from mock import Mock

class CameraTest(unittest.TestCase):
	paramUtil = ParamUtils()
	params = None

	def setUp(self):
		get_status_result =  utilsT.get_status("tests/resources/get_status.cgi")		
		self.params = self.paramUtil.parse(get_status_result)

	def test_motion_alert_activated(self):
		url = "192.168.1.105:80"		
		cam = Camera(url)
		cam.get_status = Mock(return_value=self.params)
		self.assertTrue(cam.motion_detected())

	def test_motion_alert_not_activated(self):
		url = "192.168.1.101"	
		cam = Camera(url)
		newParams = self.params
		newParams["alarm_status"] = "0"
		cam.get_status = Mock(return_value=self.params)
		self.assertFalse(cam.motion_detected())

	def system_get_cam_alert_not_activated(self):
		url = "192.168.1.101"	
		cam = Camera(url)		
		self.assertFalse(cam.motion_detected())
		
