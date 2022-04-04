#### Importing Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt

#### Loading the Image
image = cv2.imread("rectangle.jpg")

#### Converting into gray scale image
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edged = cv2.Canny(image, 30, 200)

#### Finding the contours
contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print("Number of Contours",len(contours))


### Drawing the contours
cv2.drawContours(image, contours, 1,(0,255,0),3)
for cnt in contours:
### Getting the bounding Rectangle
    x,y,w,h = cv2.boundingRect(cnt)

    ### Draw the rectangle around the object
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)

    #### Calculating the minimum Area Bounding Rectangle
    rect = cv2.minAreaRect(cnt)
    print(rect)

    box = cv2.boxPoints(rect)
    box = np.int0(box)
    print(box)
    cv2.drawContours(image,[box],-1,(0,0,255),2)
  
#         width, height = 300,100
#         pts1 = np.float32(b)
#         pts2 = np.float32([[0,0], [width,0],[0,height],[width,height]])
#         matrix = cv2.getPerspectiveTransform(pts1,pts2)
#         ouput = cv2.warpPerspective(image,matrix,(width,height))


##### Displaying the Image
    cv2.imshow("Result",image)
cv2.waitKey()
cv2.destroyAllWindows()