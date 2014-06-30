import logging



def initLogger():
	# create logger 
	logger = logging.getLogger('cam')
	logger.setLevel(logging.DEBUG)

	# create file handler which logs even debug messages
	file_handler = logging.FileHandler('cam.log')
	file_handler.setLevel(logging.DEBUG)

	# create console handler with a higher log level
	console_handler = logging.StreamHandler()
	console_handler.setLevel(logging.DEBUG)
	# create formatter and add it to the handlers
	formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
	file_handler.setFormatter(formatter)
	console_handler.setFormatter(formatter)
	# add the handlers to the logger
	logger.addHandler(file_handler)
	logger.addHandler(console_handler)	

	

def getLogger():
	logger = logging.getLogger('cam')
	return logger