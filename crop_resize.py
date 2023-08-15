import cv2

image = cv2.imread("cat.jpg")

image = cv2.resize(image, None, fx=0.2, fy=0.2,
                   interpolation=cv2.INTER_LINEAR)

cv2.imshow("resized image", image)
cv2.waitKey(0)
