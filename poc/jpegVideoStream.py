from SimpleCV import JpegStreamCamera, VideoStream# Import the parts we need from 	SimpleCV
from subprocess import call 
# This import is just to create the video (if you want to do something meanwhile)
from multiprocessing import Process
 
# To give the correct name to the output file
import time
 
# Imports to treat command line arguments 
import sys
import getopt

class VideoRec:

	def main(self):
		jc = JpegStreamCamera("http://192.168.1.101/videostream.cgi?user=pi&pwd=pi")
		vs = VideoStream("MyVideo2.avi",25, True)
		for i in range(0,35):
			print "loop"
			img = jc.getImage()
			print "gotimg"
			imgName = "img/img_%s.jpg"%(i)
			self.makeSaveImg = Process(target=self.saveImgToDisk, args=(img,imgName))
			self.makeSaveImg.start()
			#self.saveImgToDisk(img,imgName)
			vs.writeFrame(img)
			print i
			print "----------"

		#self.makefilmProcess = Process(target=self.saveFilmToDisk, args=("MyVideo2.avi", "MyoutputFile.mpeg"))
		#self.makefilmProcess.start()

		params = " -i {0} -c:v mpeg4 -b:v 700k -r 24 {1}".format("MyVideo2.avi", "MyoutputFile.avi")
	 
	    # run avconv to compress the video since ffmpeg is deprecated (going to be).
		call('avconv'+params, shell=True)

	def saveImgToDisk(self,img, filename):
		img.save(filename)

	def saveFilmToDisk(bufferName, outname):
	    # construct the encoding arguments
	    params = " -i {0} -c:v mpeg4 -b:v 700k -r 24 {1}".format(bufferName, outname)
	 
	    # run avconv to compress the video since ffmpeg is deprecated (going to be).
	    call('avconv'+params, shell=True)

if __name__ == '__main__':
	x = VideoRec()
	x.main() 
