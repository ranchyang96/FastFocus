import cv2
import sys
from subprocess import call
from datetime import datetime

name = sys.argv[1]
prefix = "figures/"
suffix = ".jpg"

cap = cv2.VideoCapture(0)
cap.set(3, 960)
cap.set(4, 544)

#image = cv2.imread("figures/pen_250.jpg")

def autorun(cmd):
    try:
        call(cmd,shell=True)
    except:
        print(cmd,'error')


def val(filename):
    def px(x, y):
        return int(gray[y, x])
    image = cv2.imread(filename)
    height, width = image.shape[:2]
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sum = 0
    for x in range(width-1):
        for y in range(height):
            sum += abs(px(x,y) - px(x+1,y))
    return sum

start=datetime.now()
maxval = 0
print("value at focus", maxval, datetime.now()-start)
for focus in range(0, 251, 50):
    filename = prefix + name + str(focus) + suffix
    print("capturing photo at focus", focus, datetime.now()-start)
    _, _ = cap.read()
    print("calculating function at focus", focus, datetime.now()-start)
    value = val(filename)
    print("value at focus", value, datetime.now()-start)
    if value > maxval:
        maxval = value
        maxn = focus

print(maxn, maxval)
