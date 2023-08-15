import cv2 as cv

image = cv.imread("cat.jpg")

image = cv.resize(image, (0, 0), fx=0.2, fy=0.2)

cv.imshow("Cat image", image)
cv.waitKey(0)
