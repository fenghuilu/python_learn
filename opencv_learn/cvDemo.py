
import cv2
import matplotlib
import numpy

img = cv2.imread('demo.jpg',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()