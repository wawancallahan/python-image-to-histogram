import cv2
import numpy as np
from matplotlib import pyplot as plt

# Grayscale
gray_img = cv2.imread('./assets/peko.png', cv2.IMREAD_GRAYSCALE)

# width, height = gray_img.shape
# hist = gray_img[0]

# for i in range(1, width):
#     hist = np.concatenate([hist, gray_img[i]])
# plt.hist(hist,256,[0,256])

cv2.imshow('Gambar',gray_img)
plt.hist(gray_img.ravel(),256,[0,256])

# hist,bins = np.histogram(gray_img,256,[0,256])
# hist = cv2.calcHist([gray_img],[0],None,[256],[0,256])
# plt.plot(hist)
plt.title('Histogram for gray scale picture')
plt.show()

# RGB
img = cv2.imread('./assets/peko.png', -1)
cv2.imshow('Gambar RGB',img)
color = ('b','g','r')
for channel,col in enumerate(color):
    histr = cv2.calcHist([img],[channel],None,[256],[0,256])
    plt.plot(histr,color = col)
    plt.xlim([0,256])
plt.title('Histogram for color scale picture')
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()