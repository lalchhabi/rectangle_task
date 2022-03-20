import cv2
import numpy as np
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 7))
font = cv2.FONT_HERSHEY_TRIPLEX
image = cv2.imread('rectangle.jpg', cv2.IMREAD_COLOR)
img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edged = cv2.Canny(img, 30, 200)
contours,hierarchy= cv2.findContours(edged,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
for cnt in contours : 
    approx = cv2.approxPolyDP(cnt, 0.09 * cv2.arcLength(cnt, True), True)
    cv2.drawContours(image, [approx], -1, (0, 255,0), 3)
    n = approx.ravel()
    i = 0
    for j in n :
        
        if(i % 2 == 0):
            
            x = n[i]
            y = n[i + 1]
            # String containing the co-ordinates.
            string = str(x) + " " + str(y) 
            if(i == 0):
                
                cv2.putText(image, string, (x, y),font, 0.5, (0, 0, 0))
                print(x,y)
                
            else:
               
                cv2.putText(image, string, (x, y), font, 0.5, (0, 0, 0)) 
                print(x,y)
        i = i + 1

#### For first Rectangle
pts1 = np.float32([[49,26],[165,56],[42,58],[158,87]])


for x in range(0,4):
    cv2.circle(img,(int(pts1[x][0]), int(pts1[x][1])),5,(0,0,255),cv2.FILLED)
    
width1, height1 = 300,100
pts2 = np.float32([[0,0], [width1,0],[0,height1],[width1,height1]])
matrix1 = cv2.getPerspectiveTransform(pts1,pts2)
output1 = cv2.warpPerspective(img, matrix1, (width1, height1))


### For Second Rectangle
pts3 = np.float32([[256,48],[367,19],[269,100],[380,72]])

for x in range(0,4):
    cv2.circle(img,(int(pts3[x][0]), int(pts3[x][1])),5,(0,0,255),cv2.FILLED)

width2, height2 = 300,100
pts4 = np.float32([[0,0], [width2,0],[0,height2],[width2,height2]])
matrix2 = cv2.getPerspectiveTransform(pts3,pts4)
output2 = cv2.warpPerspective(img, matrix2, (width2, height2))


### For third Rectangle
pts5 = np.float32([[18,238],[129,175],[42,281],[152,219]])

for x in range(0,4):
    cv2.circle(img,(int(pts5[x][0]), int(pts5[x][1])),5,(0,0,255),cv2.FILLED)

width3, height3 = 300,100
pts6 = np.float32([[0,0], [width3,0],[0,height3],[width3,height3]])
matrix3 = cv2.getPerspectiveTransform(pts5,pts6)
output3 = cv2.warpPerspective(img, matrix3, (width3, height3))

### For Fourth Rectangle
pts7 = np.float32([[290,180],[412,248],[247,258],[369,326]])

for x in range(0,4):
    cv2.circle(img,(int(pts7[x][0]), int(pts7[x][1])),5,(0,0,255),cv2.FILLED)
    

width4, height4 = 200,100
pts8 = np.float32([[0,0], [width4,0],[0,height4],[width4,height4]])
matrix4 = cv2.getPerspectiveTransform(pts7,pts8)
output4 = cv2.warpPerspective(img, matrix4, (width4, height4))


cv2.imshow("First Rectangle", output1)
cv2.imshow("Second Rectangle", output2)
cv2.imshow("Third Rectangle", output3)
cv2.imshow("Forth Rectangle", output4)

if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()





