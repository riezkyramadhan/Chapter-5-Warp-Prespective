import cv2
import numpy as np 

width,height =700,700

img = cv2.imread("card.png")
print(img.shape)

pts1 = np.float32([[111,129],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)
img_output = cv2.warpPerspective(img,matrix, (width,height))

cv2.imshow("img_output", img_output)
cv2.imshow("image", img)
cv2.waitKey(0)