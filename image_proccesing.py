#IMAGE PROCESSING IN PYTHON
#1.READ THE IMAGE

import cv2
img=cv2.imread('image.jpg')
cv2.imshow('python',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
