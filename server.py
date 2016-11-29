from flask import Flask, render_template
import os
from threadcamera import MyThread

dir_path = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)
myThread1 = MyThread()
myThread1.setName('CameraThread')


#get list of images from static folder
def getFileList():
    out_fileList = []
    staticFolder = dir_path+'/static'
    out_fileList = os.listdir(staticFolder)
    return out_fileList

#flask server
@app.route('/')
def index():
    return "hello world!  flask server served on pi"

@app.route('/images')
def staticDirectory():
    fileList = getFileList()
    print (fileList)
    return render_template('images.html', imageFiles=fileList)

#main body/threads
if __name__ == '__main__':
    myThread1.start()
    app.run(host='0.0.0.0')
    myThread1.join()

