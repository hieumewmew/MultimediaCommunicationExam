import cv2
import numpy as np

image = cv2.imread('image.png')
RGBA_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
# print(RGBA_image.shape)

cv2.imwrite('test_R.jpg', RGBA_image[...,0])
cv2.imwrite('test_G.jpg', RGBA_image[...,1])
cv2.imwrite('test_B.jpg', RGBA_image[...,2])
cv2.imwrite('test_A.jpg', RGBA_image[...,3])

