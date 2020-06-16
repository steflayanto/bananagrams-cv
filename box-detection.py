import cv2
import numpy as np
from utils import *

img = cv2.imread("canny.png", cv2.IMREAD_GRAYSCALE)
img_col = cv2.imread(r"C:\Users\Stefa\Desktop\Bananagram Solver\bananagrams-cv\imgs/2.jpg", cv2.IMREAD_COLOR)

rho = 1 # pixel dist resolution
theta = np.pi/180 # angle resolution in radians (pi / 64)
threshold = 70

lines = cv2.HoughLinesP(img, rho, theta, threshold, minLineLength=30, maxLineGap=20)
print(len(lines))
# print(lines)
drawing = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)
# cv2.namedWindow("img", cv2.WINDOW_NORMAL)
print(lines[0].shape)
for line in lines:
    line = line.reshape((2,2))
    print(line)
    cv2.line(img_col, tuple(line[0]), tuple(line[1]), color=(0,0,255), thickness=5)
# cv2.imshow("img", img)
# cv2.imshow("img", drawing)
cv2.imwrite("lines.png", img_col)
# cv2.waitKey(0)

"""
# Find contours for image, which will detect all the boxes
contours, hierarchy = cv2.findContours(img, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Sort all the contours by top to bottom.
contours, boundingBoxes = sort_contours(contours, method="top-to-bottom")

# Output
drawing = np.zeros((img.shape[0], img.shape[1], 3), dtype=np.uint8)

# Approximate contours to polygons + get bounding rects and circles
contours_poly = [None]*len(contours)
boundRect = [None]*len(contours)
# centers = [None]*len(contours)
# radius = [None]*len(contours)
for i, c in enumerate(contours):
    # contours_poly[i] = cv2.approxPolyDP(c, 3, True)
    contours_poly[i] = c
    boundRect[i] = cv2.boundingRect(contours_poly[i])
    # boundRect[i] = cv2.minAreaRect(contours_poly[i])
    # print("Area: "+ str(boundRect[i][2] * boundRect[i][3]))
    # centers[i], radius[i] = cv.minEnclosingCircle(contours_poly[i])

 # Draw polygonal contour + bonding rects + circles
for i in range(len(contours)):
    color = (0,0,255)
    cv2.drawContours(drawing, contours_poly, i, (255,255,255))
    area = boundRect[i][2] * boundRect[i][3]
    if area > 1000:
        print(area)
        cv2.rectangle(drawing, (int(boundRect[i][0]), int(boundRect[i][1])), \
            (int(boundRect[i][0]+boundRect[i][2]), int(boundRect[i][1]+boundRect[i][3])), color, 2)

# cv2.drawContours(img_col, contours, -1, (0,0,255), 3)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow("image", drawing)
cv2.waitKey(0)
cv2.imwrite("bounding_boxes.png", drawing)
# idx = 0
# for c in contours:
#     # Returns the location and width,height for every contour
#     x, y, w, h = cv2.boundingRect(c)
#     if (w > 80 and h > 20) and w > 3*h:
#         idx += 1
#         new_img = img[y:y+h, x:x+w]
#         cv2.imwrite(cropped_dir_path+str(idx) + '.png', new_img)
# # If the box height is greater then 20, widht is >80, then only save it as a box in "cropped/" folder.
#     if (w > 80 and h > 20) and w > 3*h:
#         idx += 1
#         new_img = img[y:y+h, x:x+w]
#         cv2.imwrite(cropped_dir_path+str(idx) + '.png', new_img)
"""