# import cv2 as cv
# img = cv.imread('Yash2.jpg')
# gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# eye_cascade = cv.CascadeClassifier('haarcascade_eye.xml')
# eyes = eye_cascade.detectMultiScale(gray,1.1,4)
# for x,y,w,h in eyes:
#     cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
# cv.imshow('show',img)
# cv.waitKey(0)
# cv.destroyAllWindows()

import cv2 as cv

img = cv.imread('yash_front.jpeg')
img = cv.resize(img, (500, 500))
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
eye_cascade = cv.CascadeClassifier('haarcascade_upperbody.xml')
eyes = eye_cascade.detectMultiScale(gray, 1.01, 4)
for x, y, w, h in eyes:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
cv.imshow('show', img)
cv.waitKey(0)
cv.destroyAllWindows()
