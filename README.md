IpCamMonitorSystem
==================

**NOTE:** There is still no code here, I'm just bulding it
A headles python program to monitor the activity of the ip cammera. Draft version, only works with Foscam FI8905W

UsefulLinks
-------------
**Foscam API:** http://www.foscam.es/descarga/ipcam_cgi_sdk.pdf

**How to pull H264 video from IP camera (Doesn't work with FI8905W because is not a H264):** http://blog.mikemccandless.com/2013/11/pulling-h264-video-from-ip-camera-using.html

**SimpleCV Installation:** https://simplecv.readthedocs.org/en/latest/HOWTO-Install%20on%20RaspberryPi.html?highlight=opencv

**SimpleCV on Rasbberry:** Installation on my raspberry failed so I had to use this workaround: http://www.raspberrypi.org/forums/viewtopic.php?t=56103&p=460672

**SimpleCV Cookbook:** https://simplecv.readthedocs.org/en/1.1/cookbook/# 


Installation
--------------
Install SimpleCV: See above link for more details
	sudo apt-get install ipython python-opencv python-scipy python-numpy python-setuptools python-pip
	sudo pip install https://github.com/sightmachine/SimpleCV/zipball/master
	sudo pip install svgwrite (if you the error: missing dependency svgwrite)

	
