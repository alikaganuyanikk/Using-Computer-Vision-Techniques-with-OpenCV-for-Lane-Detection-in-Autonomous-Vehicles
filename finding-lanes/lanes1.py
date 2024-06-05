import cv2

# Resmi oku
image = cv2.imread('test_image.jpg')

# Resmi göster
cv2.imshow('result',image)
cv2.waitKey(0)
