import cv2
import numpy as np
import matplotlib.pyplot as plt


def canny(image):
    gray=cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,50,150)
    return canny


image = cv2.imread('test_image.jpg')
lane_image=np.copy(image)
canny=canny(lane_image)

plt.imshow(canny)
plt.show()
