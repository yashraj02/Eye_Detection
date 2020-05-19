import cv2 as cv
cap = cv.VideoCapture(0)
while(cap.isOpened()):
    _, img = cap.read()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
    eyes = eye_cascade.detectMultiScale(gray,1.1,4)
    for x,y,w,h in eyes:
        cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
    cv.imshow('show',img)
    cv.waitKey(1)
cap.release()
cv.destroyAllWindows()