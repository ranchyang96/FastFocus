import cv2
import numpy
import sys
from subprocess import call

def autorun(cmd):
    try:
        call(cmd,shell=True)
    except:
        print(cmd,'error')

cap = cv2.VideoCapture(0)  #ignore the errors
cap.set(3, 960)        #Set the width important because the default will timeout
                       #ignore the error or false response
cap.set(4, 544)        #Set the height ignore the errors
for i in range(0, 251, 5):
    s = "v4l2-ctl --device=/dev/video0 --set-ctrl=focus_absolute="+str(i)
    autorun(s)
    r, frame = cap.read()
    name = sys.argv[1]
    s1 = "figures/" + name + str(i) + ".jpg"
    cv2.imwrite(s1, frame)
