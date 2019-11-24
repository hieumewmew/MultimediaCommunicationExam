import cv2
import numpy as np

image = cv2.imread('image.png')
RGBA_image = cv2.cvtColor(image, cv2.COLOR_BGR2BGRA)
print(RGBA_image.shape)