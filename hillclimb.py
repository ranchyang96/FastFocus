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
focus = 250
print("capturing photo at focus", focus, datetime.now()-start)
#autorun("ffmpeg -f v4l2 -i /dev/video0 -vframes 1 > tmp.txt")
_, _ = cap.read()
print("calculating function at focus", focus, datetime.now()-start)
filename = prefix + name + str(focus) + suffix
maxval = val(filename)
print("value at focus", maxval, datetime.now()-start)
step = 50
while True:
    focus = focus - step
    if focus < 0:
        focus = 0
        break
    filename = prefix + name + str(focus) + suffix
    print("capturing photo at focus", focus, datetime.now()-start)
    #autorun("ffmpeg -f v4l2 -i /dev/video0 -vframes 1 > tmp.txt")
    _, _ = cap.read()
    print("calculating function at focus", focus, datetime.now()-start)
    value = val(filename)
    print("value at focus", value, datetime.now()-start)
    if value < maxval:
        maxval = value
        break
    else:
        maxval = value
step = 10
while True:
    focus = focus + step
    if focus > 250:
        focus = 250
        break
    print("capturing photo at focus", focus, datetime.now()-start)
    #autorun("ffmpeg -f v4l2 -i /dev/video0 -vframes 1 > tmp.txt")
    _, _ = cap.read()
    print("calculating function at focus", focus, datetime.now()-start)
    filename = prefix + name + str(focus) + suffix
    value = val(filename)
    print("value at focus", value, datetime.now()-start)
    if value < maxval:
        maxval = value
        break
    else:
        maxval = value
pos = focus
step = 5
while True:
    focus = focus - step
    if focus < 0:
        focus = 0
        break
    print("capturing photo at focus", focus, datetime.now()-start)
    #autorun("ffmpeg -f v4l2 -i /dev/video0 -vframes 1 > tmp.txt")
    _, _ = cap.read()
    print("calculating function at focus", focus, datetime.now()-start)
    filename = prefix + name + str(focus) + suffix
    value = val(filename)
    print("value at focus", value, datetime.now()-start)
    if value < maxval:
        break
    else:
        maxval = value
        pos = focus

print(pos, maxval)
