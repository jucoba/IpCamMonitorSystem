import unittest
import utilsT
from camera.camera import *
from nose.tools import *
from utils.paramUtils import *

class CameraTest(unittest.TestCase):
	paramUtil = ParamUtils()
	params = None

	def setUp(self):
		get_status_result =  utilsT.get_status("tests/resources/get_status.cgi")		
		self.params = self.paramUtil.parse(get_status_result)

	def test_motion_alert_activated(self):
		cam = Camera()
		self.assertTrue(cam.motion_detected())
		
