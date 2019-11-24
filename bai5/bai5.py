import numpy as np
from PIL import Image

len = 160
unit = len//16

chess = np.zeros((len,len,3),'uint8')
for i in range(16):
    for j in range(16):
        if i+j % 2 == 0:
            chess[i*unit:(i+1)*unit, j*unit:(j+1)*unit,:] = np.ones(shape=(unit,unit,3))*255

chess_image = Image.fromarray(chess)
chess_image.save('chess.jpg')