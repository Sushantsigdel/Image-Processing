import cv2 
import numpy
import numpy as np

img= cv2.imread('sush.jpg') 
image= cv2.resize(img,(400, 500))

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Convertion Image into 3 channel for concatenation process 
img2 = np.zeros_like(image)
img2[:,:,0] = gray_image 
img2[:,:,1] = gray_image 
img2[:,:,2] = gray_image

both_image = np.hstack([image, img2]) 
cv2.imshow('Original&Grayimage',both_image) 
cv2.waitKey(0)
cv2.destroyAllWindows()
