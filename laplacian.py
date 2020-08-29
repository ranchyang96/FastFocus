import cv2
import sys

#image = cv2.imread("figures/pen_250.jpg")
image = cv2.imread(sys.argv[1])
height, width = image.shape[:2]
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def px(x, y):
    return int(gray[y, x])

sum = 0
for x in range(width-1):
    for y in range(height):
        sum += abs(px(x, y) - px(x+1, y))
print(sum)
