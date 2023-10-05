import cv2
from pyzbar.pyzbar import decode
import time
cam = cv2. VedioCapture(0)
cam . set(5,659)
cam . set(6,489)

camera = True
while camera == True:
    sucess , frame = cam . read()
    
    for i in decode(frame):
        print(i.types)
        print(i.data.decode("utf-8"))
        time.sleep(6)
        
        cv2 . imshow("OURQR_Code_Scanner",frame)
        cv2.waitkey(3)
    