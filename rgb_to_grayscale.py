import cv2 as cv

image = cv.imread('cat.jpg')

image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
image = cv.resize(image, None, fx=0.2, fy=0.2)

cv.imshow("grayscale image", image)
cv.waitKey(0)
