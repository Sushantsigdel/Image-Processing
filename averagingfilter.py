import cv2 
import numpy as np 
img = cv2.imread('ghoda.jpg')
img = cv2.resize(img,(400, 500))
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Obtain number of rows and columns 
m, n = img.shape 
# Develop Averaging filter(3, 3) mask 
mask = np.ones([3, 3], dtype = int) 
mask = mask / 9
# Convolve the 3X3 mask over the image 
img_new = np.zeros([m, n]) 
for i in range(1, m-1): 
    for j in range(1, n-1): 
        temp = img[i-1, j-1]*mask[0, 0]+img[i-1, j]*mask[0, 1] \
        +img[i-1, j + 1]*mask[0, 2]+img[i, j-1]*mask[1, 0]+ img[i, j]*mask[1, 1] \
        +img[i, j + 1]*mask[1, 2]+img[i + 1, j-1]*mask[2, 0]+img[i + 1, j]*mask[2, 1] \
        +img[i + 1, j + 1]*mask[2, 2] 
        
        img_new[i, j]= temp
        
img_new = img_new.astype(np.uint8) 
both_image = np.hstack([img, img_new])
# Display the images
cv2.imshow('Averaging',both_image)
cv2.waitKey(0)
cv2.destroyAllWindows()