import numpy as np
import matplotlib.pyplot as plt
# Đọc vào file ảnh image.png
img = plt.imread('image.png')

'''
Thực hiện yêu cầu chuyển đổi ảnh màu sang ảnh đen trắng
'''

# Hàm chuyển đổi rgb sang đen trắng
def rgb_to_gray(rgb):
    return np.dot(rgb[...,:3], [0.2989, 0.5870, 0.1140])

# Vẽ ảnh đen trắng và lưu vào file dentrang.png
fig1 = plt.figure()
plt.axis('off')
img = plt.imread('image.png')
gray = rgb_to_gray(img)
plt.imshow(gray, cmap=plt.get_cmap('gray'), vmin=0, vmax=1)
plt.show()
fig1.savefig('dentrang.png')

'''
Thực hiện việc tách ảnh thành 3 kênh R, G, B
'''

# Thực hiện tạo red channel và lưu vào file redchannel.png
r = img.copy()
# set green and blue channels to 0
r[:, :, 1] = 0
r[:, :, 2] = 0
fig2 = plt.figure()
plt.axis('off')
plt.imshow(r)
fig2.savefig('redchannel.png')

# Thực hiện tạo green channel và lưu vào file greenchannel.png
g = img.copy()
# set blue and red channels to 0
g[:, :, 0] = 0
g[:, :, 2] = 0
fig3 = plt.figure()
plt.axis('off')
plt.imshow(g)
fig3.savefig('greenchannel.png')

# Thực hiện tạo blue channel và lưu vào file bluechannel.png
b = img.copy()
# set blue and green channels to 0
b[:, :, 0] = 0
b[:, :, 1] = 0
fig4 = plt.figure()
plt.axis('off')
plt.imshow(b)
fig4.savefig('bluechannel.png')

'''
Thực hiện tổ hợp 3 ảnh R, G, B thành ảnh gốc
'''
red = plt.imread('redchannel.png')
green = plt.imread('greenchannel.png')
blue = plt.imread('bluechannel.png')
result = red.copy()
result[:, :, 1] = green[:, :, 1]
result[:, :, 2] = blue[:, :, 2]

# Thực hiện vẽ và lưu ảnh vào file rgb.png
fig5 = plt.figure()
plt.axis('off')
plt.imshow(result)
fig5.savefig('rgb.png')


