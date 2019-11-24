import numpy as np
from PIL import Image

rainbow = np.zeros((521,512,3),'uint8')

for i in range(0,256):
    rainbow[:,i,0] = 255-i
    rainbow[:,i,1] = 0+i
for i in range(256,512):
    rainbow[:,i,1] = 255-i
    rainbow[:,i,2] = 0+i 

image = Image.fromarray(rainbow)
image.save('rainbow.jpg')    