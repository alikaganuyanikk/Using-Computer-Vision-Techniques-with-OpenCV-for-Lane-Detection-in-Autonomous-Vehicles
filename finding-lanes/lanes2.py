import cv2
import numpy as np


# Resmi oku
image = cv2.imread('test_image.jpg')
lane_image=np.copy(image) #dizimizi yeni bir değişkene kopyalıyoruz.
#görüntüde yaptığımız herhangi bir değişiklik orijinale yansımasın diye
gray=cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
blur=cv2.GaussianBlur(gray,(5,5),0)
# Resmi göster
cv2.imshow('result', blur)
cv2.waitKey(0)
