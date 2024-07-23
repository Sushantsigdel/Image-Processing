import cv2
import numpy as np
image = cv2.imread('sush.jpg', cv2.IMREAD_GRAYSCALE)
image = cv2.resize(image,(400, 500)) 
edges = cv2.Canny(image, 100, 200) 
output = np.hstack([image, edges])
cv2.imshow('Original Image and Edges', output) 
cv2.waitKey(0)
cv2.destroyAllWindows()
