import copy
import sys
import math
import cv2
import numpy as np

'''
For this script to work, user should select the points in the following order:

top-left
top=right
bottom-left
bottom-right

IMPORTANT NOTE: You MUST select top points of the object first. Pithagoras won't work otherwise.

'''
# circles to be posted
circles = np.zeros((4,2),np.int)

 #counting number of points we identified
counter = 0

global cache 

def create_points(event,x,y,flags, params):
    global counter
    global cache 
    global img

    if event == cv2.EVENT_LBUTTONDOWN:
        circles[counter] = x,y
        counter = counter + 1
        print(circles)
    

img = cv2.imread("images/" + sys.argv[1])

while True:

    # check if we clicked all 4 points. If so, warp the image
    if counter == 4:
        #selecting the height and the width of the final image 
        # using Pithagoras
        width = int(math.sqrt((circles[1][0])**2 + (circles[0][0])**2))
        height = int(math.sqrt((circles[2][1])**2 + (circles[0][1])**2))

        print('width: ',width)
        print('height: ', height)

        points_original_img = np.float32([circles[0],circles[1],circles[2],circles[3]])
        projectivities = np.float32([[0,0],[width,0],[0,height],[width,height]])

        H_matrix = cv2.getPerspectiveTransform(points_original_img,projectivities)

        img_output = cv2.warpPerspective(img,H_matrix,(width,height))
        # cv2.imshow("Output image: ", img_output)
        cv2.imwrite("images/warped_" + sys.argv[1],img_output)

        cv2.imshow("Output image: ",img_output)
        key = cv2.waitKey(1)
        #if we press escape, we break the loop
        if key == 27:
            break

    # Drawinglines when clicked so we have a feel of what rectangle we are making
    for x in range(0,4):
        cv2.circle(img,(circles[x][0],circles[x][1]),3,(0,255,0),cv2.FILLED)
        if x == 1 and circles[1][0] != 0 and circles[1][1] != 0 :
            cv2.line(img,(circles[0][0],circles[0][1]), (circles[x][0],circles[x][1]), (255,0,0), 3 )
        elif circles[x][0] != 0 and circles[x][1] != 0 and x == 2:
            cv2.line(img,(circles[x-2][0],circles[x-2][1]), (circles[x][0],circles[x][1]), (255,0,0), 3 )
        elif  circles[x][0] != 0 and circles[x][1] != 0 and x == 3:
            cv2.line(img,(circles[x-2][0],circles[x-2][1]), (circles[x][0],circles[x][1]), (255,0,0), 3 )
            cv2.line(img,(circles[x-1][0],circles[x-1][1]), (circles[x][0],circles[x][1]), (255,0,0), 3 )


    cv2.imshow("Original image: ",img)
    cv2.setMouseCallback("Original image: ", create_points)
    
    key = cv2.waitKey(1)
    #if we press escape, we break the loop
    if key == 27:
        break
