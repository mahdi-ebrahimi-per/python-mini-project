import cv2
import numpy as np
from random import randint
RandCol_0 = randint(0,255)
RandCol_1 = randint(0,255)
RandCol_2 = randint(0,255)
RandCol = (RandCol_0,RandCol_1,RandCol_2)
cr_blue = range(40,255)
c_blue = (200,1,1)
for i in cr_blue:
    i = cr_blue

print(c_blue)
img = np.zeros([400,800,3], np.uint8)
font = "FONT_HERSHEY_DUPLEX"
if RandCol == cr_blue:
    cv2.putText(img,"blue",(200,400),font,1,(255,255,255),5)
fill = -1
center = (0,0)
imgShapH = img.shape[0]
imhShapW = img.shape[1]
cv2.rectangle(img,center,(imhShapW,imgShapH),RandCol,fill)
cv2.imshow('RandomColor',img)
cv2.waitKey(0)


