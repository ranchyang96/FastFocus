import cv2
import sys
from subprocess import call
from datetime import datetime
import time

name = sys.argv[1]
prefix = "figures/"
suffix = ".jpg"

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

valname = 'val_'+name+'.txt'
f = open(valname, 'w')
maxn = 0
maxval = 0
for i in range(0, 51):
    focus = i*5
    filename = prefix + name + str(focus) + suffix
    value = val(filename)
    f.write(str(focus)+' '+str(value)+'\n')
    #f.flush()
    if value > maxval:
        maxval = value
        maxn = i*5
f.close()

s = 'gnuplot -e \"set terminal png; plot \'' + valname + '\' with linespoints\" > ' + name + 'plot.png'
autorun(s)

print(maxn, maxval)

