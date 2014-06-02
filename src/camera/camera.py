
class Camera():
	
	url = None
	def __init__(self, url):		
		self.url = url

	def motion_detected(self):
		return True
		