import cv2
import numpy as np

image = cv2.imread('cat.jpg')

gauss = np.random.normal(0, 1, image.size)
gauss = gauss.reshape(
    image.shape[0], image.shape[1], image.shape[2]).astype('uint8')

image = cv2.add(image, gauss)

image = cv2.resize(image, None, fx=0.2, fy=0.2)

cv2.imshow('image with noise', image)
cv2.waitKey(0)
