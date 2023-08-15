import cv2 as cv
import numpy as np
import copy

image = cv.imread("cat.jpg")

red = copy.deepcopy(image)
green = copy.deepcopy(image)
blue = copy.deepcopy(image)

red[:, :, 0] = 0
red[:, :, 1] = 0

green[:, :, 0] = 0
green[:, :, 2] = 0

blue[:, :, 1] = 0
blue[:, :, 2] = 0

red = cv.resize(red, None, fx=0.2, fy=0.2)
green = cv.resize(green, None, fx=0.2, fy=0.2)
blue = cv.resize(blue, None, fx=0.2, fy=0.2)
image = cv.resize(image, None, fx=0.2, fy=0.2)

cv.imshow("original image", image)

while True:
    key = cv.waitKey(1)
    if key != -1:
        cv.destroyAllWindows()
    if key == ord('r'):
        cv.imshow("red channel", red)
    elif key == ord('g'):
        cv.imshow("greeb channel", green)
    elif key == ord('b'):
        cv.imshow("blue channel", blue)
    elif key == ord('o'):
        cv.imshow("original image", image)
    elif key == 27:
        break
