import unittest
import utilsT
from nose.tools import *
from utils.paramUtils import *
from mock import Mock

class UtilTest(unittest.TestCase):

	paramUtil = ParamUtils()
	params = None

	def setUp(self):
		get_status_result =  utilsT.get_status("tests/resources/get_status.cgi")		
		self.params = self.paramUtil.parse(get_status_result)

	def test_parse_result_get_alarm_status(self):
		alarm_status = self.params["alarm_status"]
		self.assertEqual("0",alarm_status)

	def test_parse_result_get_alarm_alias(self):
		
		alias = self.params["alias"]
		self.assertEqual("camara1",alias)

	def test_parse_result_get_alarm_sys_ver(self):
		
		alias = self.params["sys_ver"]
		self.assertEqual("11.35.2.51",alias)

	def test_parse_result_get_alarm_sys_now(self):
		
		alias = self.params["now"]
		self.assertEqual("1398625121",alias)		


if __name__ == '__main__':
    unittest.main()
