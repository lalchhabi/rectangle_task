import os
import cv2
import math
from tqdm import tqdm

query_img = cv2.imread('rectangle.jpg')
gray_scale_image = cv2.cvtColor(query_img, cv2.COLOR_BGR2GRAY)
canny_edge = cv2.Canny(gray_scale_image, 5, 10)
contours, hierarchy = cv2.findContours(
    canny_edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
font = cv2.FONT_HERSHEY_COMPLEX
coordinates = []
final_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 150 and area < 500:
        x, y, w, h = cv2.boundingRect(contour)
        coordinates.append([(x, y), (x+w, y+h)])
        final_contours.append(contour)
        cv2.drawContours(query_img, [contour], -1,
                         (0, 255, 0), 2, lineType=cv2.LINE_AA)


final_coordinates = []
for coord in coordinates:
    if coord not in final_coordinates:
        final_coordinates.append(coord)
        (x1, y1) = coord[0]
        (x2, y2) = coord[1]
        length = x2 - x1
        breadth = y2 - y1
        diagonal = round(math.sqrt(length * length + breadth * breadth), 1)
        
        text = "length {}".format(diagonal)
        print(diagonal)
        cv2.putText(query_img, text, (x1 + 5, y1 + 5),
                    font, 0.5, (255, 0, 0))

image = cv2.rectangle(query_img, (49, 214), (142, 270), (255, 0, 0), 2)

cv2.putText(img = image,text= '2', org =(50,130),fontFace = cv2.FONT_HERSHEY_TRIPLEX, fontScale = 2,color = (0,0,0), thickness = 1)
cv2.putText(img = image,text= '3', org = (280,145), fontFace = cv2.FONT_HERSHEY_TRIPLEX, fontScale = 2, color = (0,0,0), thickness = 1)
cv2.putText(img = image,text= '4', org = (50,330), fontFace = cv2.FONT_HERSHEY_TRIPLEX, fontScale = 2, color = (0,0,0), thickness = 1)
cv2.putText(img = image,text= '1', org = (260,330), fontFace = cv2.FONT_HERSHEY_TRIPLEX, fontScale = 2, color = (0,0,0), thickness = 1)
cv2.imshow("Result", image)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()
