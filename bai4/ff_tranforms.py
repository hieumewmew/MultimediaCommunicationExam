import scipy
import matplotlib.pyplot as plt
import numpy as np
import os
from scipy import fftpack

im = plt.imread(os.path.join('bai4','test.jpg')).astype(float)
plt.figure()
plt.imshow(im, plt.cm.gray)
plt.title('Original image')

plt.savefig(os.path.join('bai4','test_fft.jpg'))