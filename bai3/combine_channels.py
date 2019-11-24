import cv2
import numpy as np


R_image = cv2.cvtColor(cv2.imread('test_R.jpg'), cv2.COLOR_BGR2GRAY)
G_image = cv2.cvtColor(cv2.imread('test_G.jpg'), cv2.COLOR_BGR2GRAY)
B_image = cv2.cvtColor(cv2.imread('test_B.jpg'), cv2.COLOR_BGR2GRAY)
A_image = cv2.cvtColor(cv2.imread('test_A.jpg'), cv2.COLOR_BGR2GRAY)

image = np.array([R_image, G_image, B_image, A_image]).transpose(1,2,0)
print(image.shape)
cv2.imwrite('image_combined.jpg', image)