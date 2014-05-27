import unittest
from nose.tools import *
from paramUtils import *

class CamTest(unittest.TestCase):

	def test_parse_result_get_alarm_status(self):
		f = open("tests/resources/get_status.cgi","r")
		get_status_result =  f.read()
		f.close()
		paramUtil = ParamUtils()
		params = paramUtil.parse(get_status_result)
		alarm_status = params["alarm_status"]
		self.assertEqual('0',alarm_status)

	def test_parse_result_get_alarm_alias(self):
                f = open("tests/resources/get_status.cgi","r")
                get_status_result =  f.read()
                f.close()
                paramUtil = ParamUtils()
                params = paramUtil.parse(get_status_result)
                alias = params["alias"]
                self.assertEqual("'camara1'",alias)


if __name__ == '__main__':
    unittest.main()
