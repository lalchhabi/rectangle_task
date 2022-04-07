#### Importing Libraries
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt
from scipy import ndimage
image_file = "rectangle.jpg"
dir_path = ""
image = cv2.imread(image_file)
height, width, _ = image.shape
print("Width: ",width)
print("Height: ",height)
split_y = 135
split_x = int(width/2)
split_ix = 0
split_iy = 0
# Splits image.
for i in range(4):
    filename = "rectangle"
    if(i==1):
        split_ix +=split_x
        split_x += split_x
    elif(i==2):
        split_iy += split_y
        split_y = height
    elif(i==3):
        split_ix=0
        split_x = int(width/2)
    filename += str(i)
    section_img = image[split_iy:split_y , split_ix:split_x]
    cv2.imwrite(os.path.join(dir_path, f"{filename}.jpg"),section_img)
    
image_list = ['rectangle0.jpg','rectangle1.jpg','rectangle2.jpg','rectangle3.jpg']
rot_angle = [195,165,210,150]
window_name = ["First","Second","Third","Forth"]
def rotate_image(input_image,rot_angle,name):
    c_image = cv2.imread(input_image)
    gray = cv2.cvtColor(c_image, cv2.COLOR_BGR2GRAY)
    edged = cv2.Canny(gray, 30, 200)
    contours, hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    print("Number of Contours",len(contours))
    cv2.drawContours(c_image, contours, -1,(0,255,0),3)
    for cnt in contours:
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),3)
        rect = cv2.minAreaRect(cnt)
        box = cv2.boxPoints(rect)
        box = np.int0(box)
        x1,y1 = box[0]
        x2,y2 = box[3]
        lines = [x1,y1,x2,y2]
        print(lines)
        cv2.drawContours(c_image,[box],-1,(0,0,255),2)
        output_img = ndimage.rotate(c_image, rot_angle)
        cv2.imshow(name,output_img)
        
#### Applying function
for i in range(4):
    rotate_image(image_list[i],rot_angle[i],window_name[i])


        
cv2.waitKey()      
cv2.destroyAllWindows()