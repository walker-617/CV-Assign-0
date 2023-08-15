import cv2 as cv

image = cv.imread('cat.jpg')

print(image.shape[0], "x", image.shape[1])
