import scipy
import matplotlib.pyplot as plt
import numpy as np

from scipy import fftpack
import cv2

path_image = 'test.jpg'
image = cv2.imread(path_image)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('test_gray.jpg', gray_image)

fft_image = fftpack.fft2(image)
cv2.imwrite('test_fft.jpg', fft_image)