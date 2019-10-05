import urllib.request as urllib2
import cv2
import numpy as np
url='http://192.168.0.52:8080/shot.jpg'

while True:

    # Use urllib to get the image and convert into a cv2 usable format
    imageResp=urllib2.urlopen(url)
    imgNp=np.array(bytearray(imageResp.read()),dtype=np.uint8)
    img=cv2.imdecode(imgNp,-1)

    # put the image on screen
    cv2.imshow('IPWebcam',img)

    #To give the processor some less stress
    if cv2.waitKey(1) == 13:
        break
    
cv2.destroyAllWindows()