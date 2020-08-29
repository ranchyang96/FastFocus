import cv2

# 1.creating a video object
video = cv2.VideoCapture(0) 
# 2. Variable
a = 0
#video.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))

video.set(cv2.CAP_PROP_AUTO_EXPOSURE,0)
video.set(cv2.CAP_PROP_EXPOSURE,-7)
'''
video.set(cv2.CAP_PROP_FOCUS, 42)
video.set(cv2.CAP_PROP_FRAME_WIDTH,2048)
video.set(cv2.CAP_PROP_FRAME_HEIGHT,1536)
video.set(cv2.CAP_PROP_SETTINGS, 0)
video.set(cv2.CAP_PROP_AUTOFOCUS, 1)
video.set(cv2.CAP_PROP_BACKLIGHT, 4)
'''

# 3. While loop
while True:
    a = a + 1
    # 4.Create a frame object
    check, frame = video.read()
    # Converting to grayscale
    #gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 5.show the frame!
    cv2.imshow("Capturing",frame)
    # 6.for playing 
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
# 7. image saving
showPic = cv2.imwrite("filename.jpg",frame)
print(showPic)
# 8. shutdown the camera
video.release()
cv2.destroyAllWindows
