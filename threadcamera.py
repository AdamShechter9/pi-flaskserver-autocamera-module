import uuid
from time import sleep
from picamera import PiCamera
import os
from threading import Thread

dir_path = os.path.dirname(os.path.realpath(__file__))

class MyThread(Thread):
    def __init__(self):
        Thread.__init__(self)
    
    def run(self):
	#myCounter = 10
	while True:
            print("in thread %s" % (self.getName()))
	    camera = PiCamera(camera_num=0, resolution=(640, 480))
            newID = uuid.uuid1()
            try:
	        camera.capture(dir_path+'/static/'+str(newID)+'.jpg')
                print("image captured "+str(newID)+'.jpg')
            finally: 
                camera.close()
	        sleep(60)
	        #myCounter -=1

