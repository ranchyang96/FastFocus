import cv2

cap = cv2.VideoCapture(0)

'''
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc('M','J','P','G'))

cap.set(cv2.CAP_PROP_FRAME_WIDTH,2048)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1536)

cap.set(cv2.CAP_PROP_SETTINGS, 0)

cap.set(cv2.CAP_PROP_FOCUS, 42)
'''

#cap.set(cv2.CAP_PROP_AUTOFOCUS, 1)

#cap.set(cv2.CAP_PROP_BACKLIGHT, 4)

#cap.set(cv2.CAP_PROP_AUTO_EXPOSURE,0)

#cap.set(cv2.CAP_PROP_EXPOSURE,-7)


while 1:
    ret, frame = cap.read()
    cv2.imshow("cap", frame)
    if cv2.waitKey(10) & 0xff == ord('q'):
        break
    cap.release()
    cv2.destroyAllWindows()
