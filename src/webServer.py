import BaseHTTPServer
from SimpleHTTPServer import SimpleHTTPRequestHandler
import pygame
from utils.loggerConfig import *

class MyServer(SimpleHTTPRequestHandler):

	pygame.mixer.init()
	pygame.mixer.music.load("src/resources/ALARM.WAV")
	
	logger = getLogger()

	def do_GET(self):
		self.send_response(200)
		self.send_header("Content-type","text/html")
		self.end_headers()
		self.wfile.write("<HTML> GET OK.<BR>")
		self.logger.info("Motion detected from %s"%(self.client_address[0]))
		pygame.mixer.music.play()



def main():
	PORT = 8000

	Handler = MyServer
	ServerClass  = BaseHTTPServer.HTTPServer

	server_address = ('', PORT)

	httpd = ServerClass(server_address, Handler)
	initLogger()
	logger = getLogger()

	logger.info("serving at port %s"%(PORT))
	httpd.serve_forever()

if __name__ == '__main__':
	main()

