import numpy as np
import matplotlib.pyplot as plt
from scipy import fftpack
from matplotlib.colors import LogNorm

im = plt.imread('test.jpg').astype(float)

plt.figure()
plt.imshow(im, plt.cm.gray)
plt.title('Original image')
plt.savefig('gray_test.jpg')


im_fft = fftpack.fft2(im)
plt.figure()
plt.imshow(np.abs(im_fft), norm=LogNorm(vmin=5))
plt.colorbar()
plt.title('Fourier transform')
plt.savefig('fft_test.jpg')

im_new = fftpack.ifft2(im_fft).real
plt.figure()
plt.imshow(im_new, plt.cm.gray)
plt.title('Reconstructed Image')
plt.savefig('reconstruct_image.jpg')