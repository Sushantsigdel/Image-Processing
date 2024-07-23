import cv2
import numpy as np
img= cv2.imread('sush.jpg') 
image= cv2.resize(img,(400, 500))

outimage= cv2.imshow('MyImage',image) 
cv2.imwrite('./Image_Processing/0_saved_img.jpg', image) 
cv2.waitKey(0)
cv2.destroyAllWindows()
