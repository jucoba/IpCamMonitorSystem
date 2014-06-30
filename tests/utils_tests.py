import unittest
import utilsT
from nose.tools import *
from utils.paramUtils import *
from utils.configUtils import *
from camera.cameraManager import *

class UtilTest(unittest.TestCase):

	paramUtil = ParamUtils()
	configUtil = ConfigUtils()
	cameraManager = CameraManager()
	params = None

	def setUp(self):
		get_status_result =  utilsT.get_status("tests/resources/get_status.cgi")		
		self.params = self.paramUtil.parse(get_status_result)

	def test_parse_result_get_alarm_status(self):
		alarm_status = self.params["alarm_status"]
		self.assertEqual("1",alarm_status)

	def test_parse_result_get_alarm_alias(self):
		
		alias = self.params["alias"]
		self.assertEqual("camara1",alias)

	def test_parse_result_get_alarm_sys_ver(self):
		
		alias = self.params["sys_ver"]
		self.assertEqual("11.35.2.51",alias)

	def test_parse_result_get_alarm_sys_now(self):
		
		alias = self.params["now"]
		self.assertEqual("1398625121",alias)

	def test_read_config_files_shouldFindFile_cam1Config(self):
		files = self.configUtil.getConfigFiles()			
		self.assertTrue("config/cam1.config" in files)

	def test_read_config_files_shouldFindFile_cam2Config(self):
		files = self.configUtil.getConfigFiles()			
		self.assertTrue("config/cam2.config" in files)


	def test_get_user_cam1(self):
		user = self.configUtil.getUser("cam1")
		self.assertEqual("pi",user)

	def test_get_pwd_cam1(self):
		pwd = self.configUtil.getPwd("cam1")
		self.assertEqual("pi",pwd)

	def test_get_url_cam1_from_ip(self):
		camera = self.cameraManager.getCam("192.168.1.101")
		self.assertEqual("192.168.1.101:8080",camera.getUrl())

	def test_config_dictionary_cam1(self):
		data = self.configUtil.getCamConfigList()
		self.assertTrue("192.168.1.101" in data, "La camara 192.168.1.101 no se encontro")

	def test_config_dictionary_cam2(self):
		data = self.configUtil.getCamConfigList()
		self.assertTrue("192.168.1.102" in data, "La configuracion de la camara 192.168.1.102 no se encontro")

	def test_manger_get_cam2(self):
		camList = self.cameraManager.loadcameras()
		self.assertTrue("192.168.1.102" in camList, "La camara 192.168.1.102 no se encontro en el manager")

	def test_manger_get_cam1(self):
		camList = self.cameraManager.loadcameras()
		self.assertTrue("192.168.1.101" in camList, "La camara 192.168.1.101 no se encontro en el manager")

	def test_manger_get_cam2_should_not_be_found(self):
		camList = self.cameraManager.loadcameras()
		self.assertTrue("192.168.1.103" not in camList, "La camara 192.168.1.103  se encontro en el manager y no deberia")

	def test_manger_get_url_cam1(self):
		camera1 = self.cameraManager.getCam("192.168.1.101")
		self.assertEqual(camera1.getUrl(), "192.168.1.101:8080")




if __name__ == '__main__':
    unittest.main()
