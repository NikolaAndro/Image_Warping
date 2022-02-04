import cv2
import numpy as np

'''
For this script to work, user should select the points in the following order:

top-left
top=right
bottom-left
bottom-right

'''
# circles to be posted
circles = np.zeros((4,2),np.int)

 #counting number of points we identified
counter = 0

def create_points(event,x,y,flags, params):
    global counter
    if event == cv2.EVENT_LBUTTONDOWN:

        circles[counter] = x,y
        counter = counter + 1
        print(circles)

img = cv2.imread("images/book_1.jpg")

while True:

    # check if we clicked all 4 points. If so, warp the image
    if counter == 4:
        #selecting the height and the width of the final image with 10 pixel paddings
        width = (circles[1][0] )-(circles[0][0])
        height = (circles[2][1] ) - (circles[0][1])

        print('width: ',width)
        print('height: ', height)

        points_original_img = np.float32([circles[0],circles[1],circles[2],circles[3]])
        projectivities = np.float32([[0,0],[width,0],[0,height],[width,height]])

        H_matrix = cv2.getPerspectiveTransform(points_original_img,projectivities)

        img_output = cv2.warpPerspective(img,H_matrix,(width,height))
        # cv2.imshow("Output image: ", img_output)
        cv2.imwrite("images/warped_book_1.jpg",img_output)
        break

    for x in range(0,4):
        cv2.circle(img,(circles[x][0],circles[x][1]),3,(0,255,0),cv2.FILLED)

    cv2.imshow("Original image: ",img)
    cv2.setMouseCallback("Original image: ", create_points)
    cv2.waitKey(1)
